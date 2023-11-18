##########################################################################
# https://www.pythonguis.com/tutorials/first-steps-qt-creator/
# https://answers.ros.org/question/393183/using-qt-designer-and-ros2-together-for-a-gui/
# Reference for initial programming in addition to a forum about PYQT GUI
###########################################################################
from castelet.CasteletWindow import Ui_CaseletWindow
import cv2
from cv_bridge import CvBridge
from functools import partial
import math
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu
import rclpy
from rclpy.qos import (
    QoSProfile,
    QoSHistoryPolicy,
    QoSReliabilityPolicy,
    QoSDurabilityPolicy,
)
from sensor_msgs.msg import Image
from std_msgs.msg import Int16
import subprocess
import sys
from turtlesim.msg import (
    Pose as TPose,
)  # This line caused an unnecessary amount of frustration
from turtlesim.srv import TeleportAbsolute, TeleportRelative, Spawn
from custom_msg.msg import Pos, ListString


class Castlet(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.node = rclpy.create_node("castlet_node")
        self.menuSelection = ""
        self.handTxt = ""
        self.fingerTxt = ""
        self.handbinding = ""
        self.castelet_ui = Ui_CaseletWindow()
        self.castelet_ui.setupUi(self)
        self.fingeruparray = []
        self.LfingersArray = []
        self.qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1,
            durability=QoSDurabilityPolicy.VOLATILE,
        )

        self.subscriptions = {
            "Cam": self.node.create_subscription(
                Image, "/MANOS/camera/raw", self.image_callback, 1
            ),
            "topic": self.node.create_subscription(
                ListString, "/MANOS/TopicDetector", self.getBindings, self.qos_profile
            ),
            "fingersup": self.node.create_subscription(
                Int16, "/MANOS/Left_Hand/fingers_up", self.guiLSelection, 1
            ),
        }
        self.spawned_turtles = []
        self.namespace = "turtle1"  # Roslaunch script param?
        self.teleport_services = {}
        self.rotate_services = {}
        self.turtlePos = Pos()
        self.positions = {}
        self.spawnTurtle = self.node.create_client(Spawn, "spawn")
        self.pose_subscriber = self.node.create_subscription(
            TPose, "/" + self.namespace + "/pose", self.update_pose, 1
        )

        self.temp2 = 0
        self.topics = []
        self.bridge = CvBridge()
        self.ros_timer = QTimer(self)
        self.ros_timer.timeout.connect(self.process_ros_messages)
        self.ros_timer.start(30)
        self.temp = False

        ###################################################################################################
        #
        #                                      MENU OPTIONS
        #
        ###################################################################################################

        self.castelet_ui.menuBindings.aboutToShow.connect(self.refreshBindings)
        self.castelet_ui.actionTurtleSim.triggered.connect(self.TurtleDemo)
        self.castelet_ui.actionPiCarChu.triggered.connect(self.run_turtleSim)

        #    def change_callback(self, sub_key, topic_type, topic, function):

    def test(self, msg):
        pass

    def guiLSelection(self, msg):
        for i in range(self.castelet_ui.LeftHand_GridLayout.count()):
            widget = self.castelet_ui.LeftHand_GridLayout.itemAt(i).widget()
            if widget is not None:
                if i == msg.data:
                    # Darken the style for the widget at the index of msg.data
                    print(f"Widget at index {i}: {widget.objectName()}")  # Print the name of the widget

                    widget.setStyleSheet(
                        """
                        color: #2c3e50;
                        font-family: 'Segoe UI', Arial, sans-serif;
                        font-size: 14pt;
                        font-weight: bold;
                        padding: 8px;
                        margin: 4px;
                        background-color: rgb(113, 200, 195);
                        border: 1px solid #bdc3c7;
                        border-radius: 4px;
                        text-align: center;
                        """
                    )
                else:
                    # Default style for other widgets
                    widget.setStyleSheet(
                        """
                        color: #2c3e50;
                        font-family: 'Segoe UI', Arial, sans-serif;
                        font-size: 14pt;
                        font-weight: bold;
                        padding: 8px;
                        margin: 4px;
                        background-color: #ecf0f1;
                        border: 1px solid #bdc3c7;
                        border-radius: 4px;
                        text-align: center;
                        """
                    )


    def run_turtleSim(self):
        subprocess.Popen(["ros2", "run", "turtlesim", "turtlesim_node"])

    def fingersUp(self, msg):
        self.fingeruparray = msg.data

    def refreshBindings(self):
        menu_bindings = self.castelet_ui.menuBindings
        self.handTxt = ""
        self.fingerTxt = ""

        self.castelet_ui.menuLeft_Hand.aboutToShow.connect(
            partial(self.handSelection, "/MANOS/Left_Hand/")
        )
        self.castelet_ui.menuRight_Hand.aboutToShow.connect(
            partial(self.handSelection, "/MANOS/Right_Hand/")
        )
        child_widgets = menu_bindings.findChildren(
            QMenu
        )  # Children of binding Lhand and RHand
        for widget in child_widgets:
            widget.triggered.connect(partial(self.handSelection, widget.title()))
            sub_children = widget.findChildren(QMenu)
            for sub_widget in sub_children:
                sub_widget.aboutToShow.connect(
                    partial(
                        self.fingerSelection, sub_widget.title() + "_pos", sub_widget
                    )
                )

    def handSelection(self, text):
        self.handTxt = text

    def fingerSelection(self, text, sub_widget):
        self.fingerTxt = text
        self.handbinding = self.handTxt + self.fingerTxt
        sub_widget.clear()
        for topic in self.topics:
            if "/MANOS/" not in topic and "/rosout" not in topic:
                action = QAction(sub_widget)
                action.setText(topic)
                # /MANOS/left_hand/pointer_pos
                action.triggered.connect(
                    partial(
                        self.change_callback,
                        self.handbinding,
                        Pos,
                        self.handbinding,
                        self.teleportMethod,
                    )
                )
                sub_widget.addAction(action)

    def getBindings(self, msg):
        self.topics = msg.data

    def change_callback(self, sub_key, topic_type, topic, function):
        # Check if the old subscription exists
        if sub_key in self.subscriptions:
            old_subscription = self.subscriptions[sub_key]
            if old_subscription:
                self.node.destroy_subscription(old_subscription)
        new_subscription = self.node.create_subscription(topic_type, topic, function, 1)
        self.subscriptions[sub_key] = new_subscription

    def get_rotate_service(self, turtle_name):
        if turtle_name not in self.rotate_services:
            service = self.node.create_client(
                TeleportAbsolute, "/" + turtle_name + "/teleport_absolute"
            )
            self.rotate_services[turtle_name] = service
        return self.rotate_services[turtle_name]

    def get_teleport_service(self, turtle_name):
        if turtle_name not in self.teleport_services:
            service = self.node.create_client(
                TeleportAbsolute, "/" + turtle_name + "/teleport_absolute"
            )
            self.teleport_services[turtle_name] = service
        return self.teleport_services[turtle_name]

    def TurtleDemo(self):
        self.teleport_services = {}

        if self.castelet_ui.actionTurtleSim.isChecked():
            self.change_callback(
                "Skel", Image, "/MANOS/camera/hand_pos", self.image_callback
            )
            self.node.destroy_subscription(self.subscriptions["Cam"])
        else:
            self.change_callback("Cam", Image, "/MANOS/camera/raw", self.image_callback)
            self.node.destroy_subscription(self.subscriptions["Skel"])

        self.raw_image_subscription = self.node.create_subscription(
            Int16, "/MANOS/Left_Hand/fingers_up", self.turtleSelection, 1
        )
        self.followme_sub = self.node.create_subscription(
            Pos, "/MANOS/Right_Hand/Pointer_pos", self.teleportMethod, 1
        )
        self.Rotatefollowme_sub = self.node.create_subscription(
            Pos, "/MANOS/Right_Hand/Pointer_pos", self.rotateTurtle, 1
        )
        self.fingersup_sub = self.node.create_subscription(
            ListString, "/MANOS/Right_Hand", self.fingersUp, 1
        )

    #################################################################################################################################
    #
    #  If this was set to a regular subscriber this would become a blocking loop. Not entirly sure why
    #
    #################################################################################################################################

    #################################################################################################################################
    #                           WITH SOME EDITS I CREATED THE FOLLOWING TO ADAPT TO MY IMPLEMENTATION                               #
    #                               http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal
    #  This is going to be Trickier than I thought. Where as the link above demonstrates being able to give it a waypoint, the way
    #  the system publishes is faster than the turtle can move. Hence why the system freezes as the buffer/queue within the system
    #  is full. You typically see the turtle just go crazy as a result.
    #################################################################################################################################

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is_
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    ###############################################################################
    #                       If I want life to be easy lol.....                        #
    ###############################################################################
    # This seems to have changed from ROS1 and ROS2.....
    # In ROS 2, service proxies provide both synchronous and asynchronous ways to
    # call a service. When you use call_async, you are making an asynchronous
    # service call, which means that your code can continue running while waiting
    # for the service response. On the other hand, if you use call, you are making
    # a synchronous service call, which blocks until a response is received or a
    # timeout occurs. I 100% can make try catches within here but I am under the
    # Assumption that the roslaunch script will prevent any sort of issues related
    # to this service not being available
    # TODO: I also have to figure out how to get to the bottoom of the world.
    # For additional context you cannot go to (0,0) nor (0,10) as the hand no longer
    # can be detected as it becomes out of frames. Possibly adding a calibration feature?

    def teleportMethod(self, msg):
        if self.fingeruparray == ["0", "1", "0", "0", "0"]:
            teleport_service = self.get_teleport_service(self.namespace)
            teleport_request = TeleportAbsolute.Request()
            teleport_request.x = 10 - (msg.x / 640) * 10
            teleport_request.y = 10 - (msg.y / 480) * 10
            teleport_request.theta = 0.0
            teleport_service.call_async(teleport_request)

    def rotateTurtle(self, msg):
        if self.fingeruparray == ["0", "1", "1", "0", "0"]:
            teleport_service = self.get_rotate_service(self.namespace)
            teleport_request = TeleportAbsolute.Request()
            teleport_request.x = self.pose.x
            teleport_request.y = self.pose.y
            teleport_request.theta = self.calculate_theta(
                10 - (msg.x / 640) * 10, 10 - (msg.y / 480) * 10
            )
            teleport_service.call_async(teleport_request)

    def calculate_theta(self, x, y):
        current_x = self.pose.x
        current_y = self.pose.y
        delta_x = x - current_x
        delta_y = y - current_y
        theta = math.atan2(delta_y, delta_x)
        return theta

    def turtleSelection(self, msg):
        val = msg.data

        if val == 1:
            self.turleSel("turtle1")
        elif val == 2:
            if "turtle2" not in self.spawned_turtles:
                self.spawned_turtles.append("turtle2")
                self.spawn_turtle("turtle2", 5.0, 3.0, 0.0)
            self.turleSel("turtle2")

        elif val == 3:
            if "turtle3" not in self.spawned_turtles:
                self.spawned_turtles.append("turtle3")
                self.spawn_turtle("turtle3", 1.0, 4.0, 0.0)
            self.turleSel("turtle3")

        elif val == 4:
            self.namespace = "turtle4"
            if "turtle4" not in self.spawned_turtles:
                self.spawned_turtles.append("turtle4")
                self.spawn_turtle("turtle4", 8.0, 8.0, 0.0)
            self.turleSel("turtle4")

        elif val == 5:
            if "turtle5" not in self.spawned_turtles:
                self.spawned_turtles.append("turtle5")
                self.spawn_turtle("turtle5", 8.0, 5.0, 0.0)
            self.turleSel("turtle5")

    def turleSel(self, name):
        if self.namespace == name:
            pass
        else:
            self.namespace = name
            self.node.destroy_subscription(self.pose_subscriber)
            self.turtlePoseSubNode = self.node.create_subscription(
                TPose,
                "/" + self.namespace + "/pose",
                self.update_pose,
                self.qos_profile,
            )

    def spawn_turtle(self, name, x, y, theta):
        request = Spawn.Request()
        request.name = name
        request.x = x
        request.y = y
        request.theta = theta
        self.spawnTurtle.call_async(request)

    def image_callback(self, msg):
        try:
            # Convert ROS Image message to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg)
            # Display the image in the QtLabel
            self.display_image(cv_image)

        except Exception as e:
            print(str(e))

    def display_image(self, cv_image):
        # Comment this line to become a smurf...
        reversed_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        reversed_image = cv2.flip(reversed_image, 1)
        # Get the image dimensions
        height, width, channel = reversed_image.shape

        # Convert the NumPy array to bytes
        bytes_per_line = 3 * width
        q_image = QImage(
            reversed_image.data.tobytes(),
            width,
            height,
            bytes_per_line,
            QImage.Format_RGB888,
        )

        # Convert the QImage to a QPixmap and set it to the QLabel
        pixmap = QPixmap.fromImage(q_image)

        # Create a QPainter to draw on the QPixmap

        painter = QPainter(pixmap)
        pen = QPen(QColor(255, 0, 0))  # Red color
        pen.setWidth(2)
        painter.setPen(pen)

        # Draw a red horizontal line to split the image
        height, _ = pixmap.height(), pixmap.width()
        painter.drawLine(0, height // 2, width, height // 2)
        painter.drawLine(width // 2, 0, width // 2, height)

        # End painting
        painter.end()

        # Set the QPixmap with the drawn line to the QLabel
        self.castelet_ui.camera_lb.setPixmap(pixmap)

    def process_ros_messages(self):
        # Process ROS messages by calling spin_once() in each timer tick
        rclpy.spin_once(self.node)


def main(args=None):
    rclpy.init(args=None)
    app = QtWidgets.QApplication(sys.argv)
    window = Castlet()
    window.show()
    app.exec_()

    # Ensure proper shutdown of ROS 2 when the application exits
    rclpy.shutdown()


if __name__ == "__main__":
    main()
