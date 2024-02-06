##########################################################################
# https://www.pythonguis.com/tutorials/first-steps-qt-creator/
# https://answers.ros.org/question/393183/using-qt-designer-and-ros2-together-for-a-gui/
# Reference for initial programming in addition to a forum about PYQT GUI
###########################################################################
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
    HistoryPolicy,
    ReliabilityPolicy,
    DurabilityPolicy,
)
from sensor_msgs.msg import Image
from castelet.CasteletWindow import Ui_CaseletWindow
from geometry_msgs.msg import Twist, Pose
from custom_msg.msg import Pos, ListString
from turtlesim.msg import Pose as TPose #This line caused an unessasary amount of frustration
from turtlesim.srv import TeleportAbsolute, TeleportRelative, Spawn
from std_msgs.msg import Int16,String
import sys
from PyQt5.QtWidgets import QLabel
SELECTED_STYLE = """
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

UNSELECTED_STYLE = """
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

class Castlet(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.node = rclpy.create_node('castelet_node')

        self.menuSelection = ""
        self.handTxt = ""
        self.fingerTxt=""      
        self.handbinding=""
        self.services = []
        
        self.castelet_ui = Ui_CaseletWindow()
        self.castelet_ui.setupUi(self)
        self.castelet_ui.test.clicked.connect(self.getServiceList)
        self.qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)
        self.castelet_ui.menuLeft_Hand.aboutToShow.connect(partial(self.handSelection, '/MANOS/Left_Hand/'))
        self.castelet_ui.menuRight_Hand.aboutToShow.connect(partial(self.handSelection, '/MANOS/Right_Hand/'))
        self.subscriptions = {
            'Cam':  self.node.create_subscription(Image, '/MANOS/camera/raw', self.image_callback , self.qos_profile),
            'Skel':  self.node.create_subscription(Image, '/MANOS/camera/hand_pos', self.test, self.qos_profile),
            'lfingersupgui': self.node.create_subscription(Int16, "/MANOS/Left_Hand/fingers_up", partial(self.guiSelection,'left') , 1  ),
            'rfingersupgui': self.node.create_subscription(Int16, "/MANOS/Right_Hand/fingers_up", partial(self.guiSelection,"right") ,1  ),


        }

        self.menu_selection_publisher = self.node.create_publisher(String, '/MANOS/menuSelection', 2)
        self.bindings_selection_publisher = self.node.create_publisher(String, '/MANOS/binding', 2)
        self.binding_option_subscriber = self.node.create_subscription(ListString, '/MANOS/Services', self.getBindings, self.qos_profile)


        self.topics = []
        self.bridge = CvBridge()
        self.ros_timer = QTimer(self)
        self.ros_timer.timeout.connect(self.process_ros_messages)
        self.ros_timer.start(30)
        self.temp = False
        self.guiHelper("left")
        self.guiHelper("right")
        

###################################################################################################
#                                                                                                 #
#                                      MENU OPTIONS                                               #
#                                                                                                 #
###################################################################################################

        self.castelet_ui.menuBindings.aboutToShow.connect(self.refreshBindings)
        self.castelet_ui.actionTurtleSim.triggered.connect(self.TurtleDemo)

    def test(self, msg):
        pass
   
    def getServiceList(self):
        return self.services

    def guiSelection(self, side, msg):
        grid_layout = None

        if side == "left":
            grid_layout = self.castelet_ui.LeftHand_GridLayout
        elif side == "right":
            grid_layout = self.castelet_ui.RightHand_GridLayout  # Assuming you have a RightHand_GridLayout

        for i in range(grid_layout.count()):
            widget = grid_layout.itemAt(i).widget()
            if widget is not None:
                if i == msg.data:
                    print(f"Widget at index {i}: {widget.objectName()}") 

                    widget.setStyleSheet(SELECTED_STYLE)
                else:
                    widget.setStyleSheet(UNSELECTED_STYLE)

    def guiHelper(self, side):
        if side == "left":
            grid_layout = self.castelet_ui.LeftHand_GridLayout
        elif side == "right":
            grid_layout = self.castelet_ui.RightHand_GridLayout 
        if grid_layout is not None:
            for i in range(5):
                label = QLabel(f"{i + 1}")
                label.setStyleSheet(UNSELECTED_STYLE)  # Use the constant here
                grid_layout.addWidget(label, i, 0)     
    def run_turtleSim(self):
        subprocess.Popen(["ros2", "run", "turtlesim", "turtlesim_node"])

    def fingersUp(self, msg):
        self.fingeruparray = msg.data

    def refreshBindings(self):
        self.menu_bindings = self.castelet_ui.menuBindings
        self.handTxt = ""
        self.fingerTxt = ""
        child_widgets = self.menu_bindings.findChildren(QMenu) 
         
        for widget in child_widgets:
            if not widget.signalsBlocked():
                widget.triggered.connect(partial(self.handSelection, widget.title()))
                sub_children = widget.findChildren(QMenu)

                for sub_widget in sub_children:
                  sub_widget.aboutToShow.connect(partial(self.fingerSelection, sub_widget.title()+"_pos",sub_widget))

    def handSelection(self, text): 
        self.handTxt=text   


        self.castelet_ui.menuLeft_Hand.aboutToShow.connect(
            partial(self.handSelection, "/MANOS/Left_Hand/")
        )
        self.castelet_ui.menuRight_Hand.aboutToShow.connect(
            partial(self.handSelection, "/MANOS/Right_Hand/")
        )
        child_widgets = self.menu_bindings.findChildren(
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
        print(text)
        self.handTxt = text

    def fingerSelection(self, text, sub_widget):
        self.fingerTxt = text
        self.handbinding = self.handTxt + self.fingerTxt
        sub_widget.clear()

        for topic in self.topics:
            if "/MANOS/" not in topic and "/rosout" not in topic:
                action = QAction(sub_widget)
                action.setText(topic)
                action.triggered.connect(partial(self.bindings, self.handbinding, topic))
# =======
#                 # /MANOS/left_hand/pointer_pos
#                 action.triggered.connect(
#                     partial(
#                         self.change_callback,
#                         self.handbinding,
#                         Pos,
#                         self.handbinding,
#                         self.teleportMethod,
#                     )
#                 )
# >>>>>>> master
                sub_widget.addAction(action)

    def getBindings(self, msg):
        self.topics = msg.data

    def bindings(self, selection, topic):
        self.menuselection = String()
        self.menuselection.data=selection

        self.bindingsSelection = String()
        self.bindingsSelection.data = topic
        
        self.bindings_selection_publisher.publish(self.bindingsSelection)
        self.menu_selection_publisher.publish(self.menuselection)

    def change_callback(self, sub_key, topic_type, topic, function):
        # Check if the old subscription exists
        if sub_key in self.subscriptions:
            old_subscription = self.subscriptions[sub_key]
            if old_subscription:
                self.node.destroy_subscription(old_subscription)
        new_subscription = self.node.create_subscription(topic_type, topic, function, 1)
        self.subscriptions[sub_key] = new_subscription

            
    def TurtleDemo(self):
        if self.castelet_ui.actionTurtleSim.isChecked():
            self.change_callback(
                "Skel", Image, "/MANOS/camera/hand_pos", self.image_callback
            )
            self.node.destroy_subscription(self.subscriptions["Cam"])
        else:
            self.change_callback("Cam", Image, "/MANOS/camera/raw", self.image_callback)
            self.node.destroy_subscription(self.subscriptions["Skel"])

        # Pass the Node instance to TurtleSimControl
 

    # def turtleSelection(self, msg):
    #     val = msg.data
    #     if val == 1:
    #         self.namespace = 'turtle1'

    #     elif val == 2:
    #         self.namespace = 'turtle2'
    #         if 'turtle2' not in self.spawned_turtles:
    #             self.spawned_turtles.append('turtle2')
    #             self.spawn_turtle('turtle2', 5.0, 3.0, 0.0)
    #     elif val == 3:
    #         self.namespace = 'turtle3'
    #         if 'turtle3' not in self.spawned_turtles:
    #            self.spawned_turtles.append('turtle3')
    #            self.spawn_turtle('turtle3', 1.0, 4.0, 0.0)
    #     elif val == 4 :
    #         self.namespace = 'turtle4'
    #         if 'turtle4' not in self.spawned_turtles:
    #             self.spawned_turtles.append('turtle4')
    #             self.spawn_turtle('turtle4', 8.0, 8.0, 0.0)
    #     elif val == 5:
    #         self.namespace = 'turtle5'
    #         if 'turtle5' not in self.spawned_turtles:
    #            self.spawned_turtles.append('turtle5')
    #            self.spawn_turtle('turtle5', 8.0, 5.0, 0.0)
    #     return self.namespace


    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg)
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

        pixmap = QPixmap.fromImage(q_image)
        painter = QPainter(pixmap)
        pen = QPen(QColor(255, 0, 0)) 
        pen.setWidth(2)
        painter.setPen(pen)
        height, _ = pixmap.height(), pixmap.width()
        painter.drawLine(0, height // 2, width, height // 2)
        painter.drawLine(width // 2, 0, width // 2, height)

        painter.end()

        self.castelet_ui.camera_lb.setPixmap(pixmap)

    def process_ros_messages(self):
        rclpy.spin_once(self.node)

def main(args=None):
    rclpy.init(args=None)
    app = QtWidgets.QApplication(sys.argv)
    window = Castlet()
    window.show()
    app.exec_()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
