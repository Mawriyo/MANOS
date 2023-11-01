##########################################################################
# https://www.pythonguis.com/tutorials/first-steps-qt-creator/
# https://answers.ros.org/question/393183/using-qt-designer-and-ros2-together-for-a-gui/
# Reference for initial programming in addition to a forum about PYQT GUI 
###########################################################################

from curses import COLOR_RED
from functools import partial
from math import pow, atan2, sqrt
import math
import threading
import time
import cv2
from src.castelet.turtleSimControl.TurtleSimControl import TurtleSimControl
import rclpy
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
import sys
from cv_bridge import CvBridge
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QAction, QWidget,QMenu
from sensor_msgs.msg import Image
from castelet.CasteletWindow import Ui_CaseletWindow
from geometry_msgs.msg import Twist, Pose
from custom_msg.msg import Pos, ListString
from turtlesim.msg import Pose as TPose #This line caused an unessasary amount of frustration
from turtlesim.srv import TeleportAbsolute, TeleportRelative, Spawn
from std_msgs.msg import Int16


class Castlet(QMainWindow,):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.node = rclpy.create_node('castelet_node')
        # self.turtleSimControl = rclpy.
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
          #  'left_hand': self.node.create_subscription(Pos, '/MANOS/Left_Hand/Pointer_pos', self.test, self.qos_profile),
           # 'rhand': self.node.create_subscription(Pos, '/MANOS/Right_Hand/Pointer_pos', self.test, self.qos_profile),
            'Cam':  self.node.create_subscription(Image, '/MANOS/camera/raw_image', self.image_callback , self.qos_profile),
            #'Skel':  self.node.create_subscription(Image, '/MANOS/camera/hand_pos', self.test, self.qos_profile),
            'temp':  self.node.create_subscription(ListString, '/MANOS/ServiceDetector', self.test, self.qos_profile),

        }
        self.spawned_turtles = []  
        self.namespace = 'turtle1' #Roslaunch script param? 


        self.velocity_publisher = self.node.create_publisher(Twist, '/'+ self.namespace + '/cmd_vel', 2)
        # self.pose_subscriber = self.node.create_subscription(TPose, '/'+ self.namespace + '/pose', self.update_pose, self.qos_profile)
        self.binding_option_subscriber = self.node.create_subscription(ListString, '/MANOS/ServiceDetector', self.getBindings, self.qos_profile)
        # self.teleport_service = self.node.create_client(TeleportAbsolute, '/'+ self.namespace + '/teleport_absolute')
        self.spawnTurtle = self.node.create_client(Spawn, 'spawn' )
        self.turtleSimControl = TurtleSimControl()

        self.topics = []
        self.bridge = CvBridge()
        self.ros_timer = QTimer(self)
        self.ros_timer.timeout.connect(self.process_ros_messages)
        self.ros_timer.start(30)

        # t1 = threading.Thread(target=self.process_ros_messages2)
        # t1.start()
        self.temp = False
        

###################################################################################################
#                                                                                                 #
#                                      MENU OPTIONS                                               #
#                                                                                                 #
###################################################################################################
        self.castelet_ui.menuBindings.aboutToShow.connect(self.refreshBindings)
        self.castelet_ui.actionTurtleSim.triggered.connect(self.TurtleDemo)
        #    def change_callback(self, sub_key, topic_type, topic, function):

    def test(self,msg):
        # print(msg) 
        # print(str(msg.data))
        pass
   #     self.filtered_service_list = [(service_name, service_type) for service_name, service_type in  self.services
                                # if any(keyword in service_name for keyword in self.keywords)]

    def getServiceList(self):
        return self.services

    def refreshBindings(self):
        menu_bindings = self.castelet_ui.menuBindings
        self.handTxt = ""
        self.fingerTxt = ""
        child_widgets = menu_bindings.findChildren(QMenu) 
         
        for widget in child_widgets:
        # Check if connections already exist and only establish new connections if they don't
            if not widget.signalsBlocked():
                widget.triggered.connect(partial(self.handSelection, widget.title()))
                sub_children = widget.findChildren(QMenu)

                for sub_widget in sub_children:
                  sub_widget.aboutToShow.connect(partial(self.fingerSelection, sub_widget.title()+"_pos",sub_widget))

    def handSelection(self, text): 
        self.handTxt=text   

    def fingerSelection(self, text,sub_widget):  
        self.fingerTxt=text      
        self.handbinding = self.handTxt + self.fingerTxt
        sub_widget.clear()

        for topic in self.turtleSimControl.servicess:
            print(str(topic))
            if "/MANOS/" not in topic and "/rosout" not in topic:
                action = QAction(sub_widget)
                action.setText(topic)
                #/MANOS/left_hand/pointer_pos
                action.triggered.connect(partial(self.change_callback, self.handbinding, Pos, self.handbinding, self.turtleSelection))
                sub_widget.addAction(action)


    def getBindings(self,msg):
        # print("FROM DIRECT TOPIC" + str(msg.data))
        # print("FROMT TURTLECONTROLNODE INSTANCE" + str(self.turtleSimControl.getServices()))
        self.turtleSimControl.initialize()
        if not self.temp:
            # rclpy.spin(self.turtleSimControl)
            self.temp = True
        print("FROMT BEFORE INSTANCE" )
        print(str(self.turtleSimControl.getServiceList()))
        print("FROMT TURTLECONTROLNODE INSTANCE" )

     

    def change_callback(self, sub_key, topic_type, topic, function):
        # Check if the old subscription exists
        if sub_key in self.subscriptions:
            old_subscription = self.subscriptions[sub_key]
            if old_subscription:
                self.node.destroy_subscription(old_subscription)
        new_subscription = self.node.create_subscription(topic_type, topic, function, self.qos_profile)
        self.subscriptions[sub_key] = new_subscription

            
    def TurtleDemo(self):
        # if 'Skel' in self.subscriptions and self.subscriptions['Skel']:
        #     self.node.destroy_subscription(self.subscriptions['Skel'])


        if self.castelet_ui.actionTurtleSim.isChecked():
            self.change_callback('Skel', Image, '/MANOS/camera/hand_pos', self.image_callback)
            self.node.destroy_subscription(self.subscriptions['Cam'])
        else:
            self.change_callback('Cam', Image, '/MANOS/camera/raw_image', self.image_callback)
            self.node.destroy_subscription(self.subscriptions['Skel'])

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
            # Convert ROS Image message to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg)
            # Display the image in the QtLabel
            self.display_image(cv_image)

        except Exception as e:
            print(str(e))

    def display_image(self, cv_image):
        # Comment this line to become a smurf...
        reversed_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        reversed_image = cv2.flip(reversed_image,1)
        # Get the image dimensions
        height, width, channel = reversed_image.shape

        # Convert the NumPy array to bytes
        bytes_per_line = 3 * width
        q_image = QImage(
            reversed_image.data.tobytes(),
            width,
            height,
            bytes_per_line,
            QImage.Format_RGB888
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
        painter.drawLine(width//2, 0, width//2, height)

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

if __name__ == '__main__':
    main()
