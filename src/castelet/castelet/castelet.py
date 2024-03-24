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
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication
import rclpy
from rclpy.qos import (
    QoSProfile,
    HistoryPolicy,
    ReliabilityPolicy,
    DurabilityPolicy,
)
from .CustomLabel import CalibrationLabel 
from .Toast_Object import Toast
from castelet.CasteletWindow import Ui_CaseletWindow
from geometry_msgs.msg import Twist, Pose
from custom_msg.msg import Pos, ListString
from turtlesim.msg import Pose as TPose #This line caused an unessasary amount of frustration
from turtlesim.srv import TeleportAbsolute, TeleportRelative, Spawn
from std_msgs.msg import Int16,String
from sensor_msgs.msg import Image
from .BindingDialog import BindingDialog
import sys
from PyQt5.QtWidgets import QLabel

# .TODO: Python Debugger for freezing gui. BLocking method? 
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
        self.currentHand=None
        self.services = []
        # self.calibrationLabel = CalibrationLabel(self)
        self.castelet_ui = Ui_CaseletWindow()
        # self.castelet_ui.camera_lb = self.calibrationLabel
        self.castelet_ui.setupUi(self)

        self.qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)

        self.subscriptions = {
            'Cam':  self.node.create_subscription(Image, '/MANOS/camera/raw', self.image_callback , self.qos_profile),
            'Skel':  self.node.create_subscription(Image, '/MANOS/camera/hand_pos', self.test, self.qos_profile),
            'lfingersupgui': self.node.create_subscription(Int16, "/MANOS/Left_Hand/fingers_up", partial(self.guiSelection,'left') , 1  ),
            'rfingersupgui': self.node.create_subscription(Int16, "/MANOS/Right_Hand/fingers_up", partial(self.guiSelection,"right") ,1  ),

        }
        
        self.hand_selection = self.node.create_publisher(String,  "/MANOS/Manager/HandSelection", 2)
        self.typePub = self.node.create_publisher(String,"/MANOS/Manager/TypeSelection",2)
        self.array_publisher = self.node.create_publisher(String,"/MANOS/Manager/FingerSelection", 2)
        self.bindings_selection_publisher = self.node.create_publisher(String, "/MANOS/Manager/TopicSelection", 2)#eywords passed by manos manager such as /spawn, kill etc
        self.binding_option_subscriber = self.node.create_subscription(ListString, '/MANOS/Manager/Services', self.getBindings, self.qos_profile)
        # self. = self.node.create_subscription(ListString, '/MANOS/Services', self.getBindings, self.qos_profile)

        self.castelet_ui.menuLeft_Hand.aboutToShow.connect(
            partial(self.populateTopics, self.castelet_ui.menuLeft_Hand, "/MANOS/Left_Hand/")
        )
        self.castelet_ui.menuRight_Hand.aboutToShow.connect(
            partial(self.populateTopics, self.castelet_ui.menuRight_Hand, "/MANOS/Right_Hand/")
        )
        self.count = 0
        self.topics = []
        self.bridge = CvBridge()
        self.ros_timer = QTimer(self)
        self.ros_timer.timeout.connect(self.process_ros_messages)
        self.ros_timer.start(30)
        self.temp = False
        self.guiHelper("left")
        self.guiHelper("right")

        self.castelet_ui.menuBindings.aboutToShow.connect(self.refreshBindings)
        self.castelet_ui.actionTurtleSim.triggered.connect(self.TurtleDemo)
    
    
    def bindings(self, finger_combination, topic, hand):
        self.fingersListArray = ListString()
        self.fingersListArray.data = finger_combination
        self.bindingsSelection = String()
        self.bindingsSelection.data = topic  # keywords passed by manos manager such as /spawn, kill etc
        self.bindings_selection_publisher.publish(self.bindingsSelection)
        self.array_publisher.publish(self.fingersListArray)

    def calibrate(self):
        self.toast = Toast(self, "This is a toast message!", 3000)
        self.toast.show(self)

    def change_callback(self, sub_key, topic_type, topic, function):
        print(f"Changing callback for {sub_key}")      
        if sub_key in self.subscriptions:
            old_subscription = self.subscriptions[sub_key]
            if old_subscription:
                self.node.destroy_subscription(old_subscription)
        new_subscription = self.node.create_subscription(topic_type, topic, function, 1)
        self.subscriptions[sub_key] = new_subscription

    def display_image(self, cv_image):
        print("Displaying image")
        reversed_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        reversed_image = cv2.flip(reversed_image, 1)
        height, width, channel = reversed_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(
            reversed_image.data.tobytes(),
            width,
            height,
            bytes_per_line,
            QImage.Format_RGB888,
        )
        pixmap = QPixmap.fromImage(q_image)
        self.castelet_ui.camera_lb.setPixmap(pixmap)

    def getBindings(self, msg):
        print ("AHHHHHHHHHHHHHHHHHH")
        print(str(msg.data))
        self.topics = msg.data

    def getServiceList(self):
        return self.services

    def guiHelper(self, side):
        if side == "left":
            grid_layout = self.castelet_ui.LeftHand_GridLayout
        elif side == "right":
            grid_layout = self.castelet_ui.RightHand_GridLayout
        if grid_layout is not None:
            for i in range(5):
                label = QLabel(f"{i + 1}")
                label.setObjectName(f"{side}{i + 1}")
                label.setStyleSheet(UNSELECTED_STYLE)
                grid_layout.addWidget(label, i, 0)

    def guiSelection(self, side, msg):
        print("gui selection image")

        grid_layout = None
        if side == "left":
            grid_layout = self.castelet_ui.LeftHand_GridLayout
        elif side == "right":
            grid_layout = self.castelet_ui.RightHand_GridLayout
        self.currentHand = side
        for i in range(grid_layout.count()):
            widget = grid_layout.itemAt(i).widget()
            if widget is not None:
                if i == msg.data:
                    print(f"Widget at index {i}: {widget.objectName()}")
                    widget.setStyleSheet(SELECTED_STYLE)
                else:
                    widget.setStyleSheet(UNSELECTED_STYLE)

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg)
            self.display_image(cv_image)
        except Exception as e:
            print(str(e))

    def keyPressEvent(self, event):
        pass
        # if event.key() == Qt.Key_C and (event.modifiers() & Qt.ControlModifier):
        #     self.node.destroy_node()
        #     rclpy.shutdown()
        #     QApplication.instance().quit()

    def newBinding(self):
        dialog = BindingDialog(self.topics)
        if dialog.exec_():
            self.fingersListArray = ListString()
            self.fingersListArray.data = dialog.getSelectedFingerCombination()
            self.bindingsSelection = String()
            self.bindingsSelection.data = dialog.getSelectedTopic()  # keywords passed by manos manager such as /spawn, kill etc
            self.bindings_selection_publisher.publish(self.bindingsSelection)
            self.array_publisher.publish(self.fingersListArray)

    def populateTopics(self, menu, handTxt):
        self.handTxt = handTxt
        menu.clear()
        print(self.topics)
        for topic in self.topics:
            if "/MANOS/" not in topic and "/rosout" not in topic:
                action = QAction(menu)
                action.setText(topic)
                action.triggered.connect(partial(self.topicSelected, topic, handTxt))
                menu.addAction(action)
        if self.selections:
            removeMenu = QMenu("Remove Selection", menu)
            menu.addMenu(removeMenu)
            for selection in self.selections:
                removeAction = QAction(removeMenu)
                removeAction.setText(selection)
                removeAction.triggered.connect(partial(self.removeSelection, selection))
                removeMenu.addAction(removeAction)

    def process_ros_messages(self):
        rclpy.spin_once(self.node)
        self.count+=1
        print("success " + str(self.count))




    def refreshBindings(self):
        self.menu_bindings = self.castelet_ui.menuBindings
        self.handTxt = ""
        self.selections = []

    def removeSelection(self, topic):
        if topic in self.selections:
            self.selections.remove(topic)
            self.refreshBindings()
            
    def test(self, msg):
        pass

    def topicSelected(self, topic, hand):
        print(hand)
        dialog = BindingDialog(topic, hand)
        if dialog.exec_():
            self.msgtype = dialog.getMsgType()  # doesn't do anything for now
            self.bindings_selection_publisher.publish(dialog.getSelectedTopic())  # keywords passed by manos manager such as /spawn, kill etc
            self.array_publisher.publish(dialog.getSelectedFingerCombination())  # sends the array of fingers to the manos manager to handle
            self.hand_selection.publish(dialog.getSelectedHand())
            self.typePub.publish(dialog.getMsgType())
            if len(self.selections) < 3:
                self.selections.append(topic)
                self.refreshBindings()  # Refresh to update the remove selections submenu

    def TurtleDemo(self):
        if self.castelet_ui.actionTurtleSim.isChecked():
            self.change_callback(
                "Skel", Image, "/MANOS/camera/hand_pos", self.image_callback
            )
            self.node.destroy_subscription(self.subscriptions["Cam"])
        else:
            self.change_callback("Cam", Image, "/MANOS/camera/raw", self.image_callback)
            self.node.destroy_subscription(self.subscriptions["Skel"])

def main(args=None):
    rclpy.init(args=None)
    app = QtWidgets.QApplication(sys.argv)
    window = Castlet()
    window.show()
    try:
        app.exec_()
    except KeyboardInterrupt:
        print("AHHHHHHH")
        window.node.destroy_node()
        rclpy.shutdown()
        app.quit()
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()
