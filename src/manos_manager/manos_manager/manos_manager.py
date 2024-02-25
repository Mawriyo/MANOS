import math
import threading
from custom_ros_controller.custom_ros_controller import TurtleSimControl
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, Spawn, Kill
from turtlesim.msg import Pose as TPose #This line caused an unessasary amount of frustration
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from custom_msg.msg import ListString,Pos, MANOSBundle
from std_msgs.msg import Int16, String
from functools import partial

finger_combinations = {
    "[1, 0, 0, 0, 0]": "Thumb_pos",
    "[0, 1, 0, 0, 0]": "Pointer_pos",
    "[0, 0, 1, 0, 0]": "Middle_pos",
    "[0, 0, 0, 1, 0]": "Ring_pos"  ,
    "[0, 0, 0, 0, 1]": "Pinky_pos" ,
    "[1, 1, 0, 0, 0]": "Pointer_pos",
    "[0, 1, 1, 0, 0]": "Pointer_pos",
    "[0, 0, 1, 1, 0]": "Middle_pos",
    "[0, 0, 0, 1, 1]": "Ring_pos",
    "[1, 1, 1, 0, 0]": "Middle_pos",
    "[0, 1, 1, 1, 0]": "Middle_pos",
    "[0, 0, 1, 1, 1]": "Middle_pos",
    "[1, 1, 1, 1, 0]": "Middle_pos",
    "[0, 1, 1, 1, 1]": "Middle_pos",
    "[1, 1, 1, 1, 1]": "Middle_pos",
}
class Manos_Manager(Node):
    def __init__(self):
        super().__init__('manos_manager')
        self.currentTopic = ""
        self.menuItem = ""
        self.fingerarray = []
        self.finger_combinations_dict = {}
        self.qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)

        self.bindingSelection = self.create_subscription(String, "/MANOS/binding", self.checkMenuSelection, self.qos_profile) #"users selected /spawn"
        self.fingersArraySub = self.create_subscription(String, "/MANOS/arrayFingers", self.fingerSelection, self.qos_profile) #[1][1][1][1][1]
        self.handSelectionSub = self.create_subscription(String, "/MANOS/handSelection", self.handSelection, self.qos_profile) # left or right
        self.typeSub = self.create_subscription(String, "/MANOS/TypeSub", self.SubCreation, self.qos_profile) # left or right

    def checkMenuSelection(self, msg):
        self.menuItem = msg.data
        print(str(self.menuItem))
  

    def handSelection(self,msg):
        self.currenthand = msg.data
        print(str(self.currenthand)+"test")
        
    def fingerSelection(self, msg):
        self.fingerarray = msg.data
        if self.fingerarray in self.finger_combinations_dict:
            del self.finger_combinations_dict[self.fingerarray]
            print("Removed existing bind" + str(self.fingerarray))
        else:
            self.finger_combinations_dict[self.fingerarray] = True


    def change_callback(self, sub_key, topic_type, topic, function):
        if sub_key in self.subscriptions:
            old_subscription = self.subscriptions[sub_key]
            if old_subscription:
                self.destroy_subscription(old_subscription)
        new_subscription = self.create_subscription(topic_type, topic, function, self.qos_profile)
        self.subscriptions[sub_key] = new_subscription
        
    def SubCreation(self, msg):
        if msg.data == 'Pos':
            string = self.currenthand + self.get_finger_name(self.fingerarray)
            self.create_subscription(Pos(), string , partial(self.handle_request, self.menuItem), self.qos_profile)
        
        # if msg.data == "Fingersup":
            
    
    def get_finger_name(self, finger_array):
        finger_key = str(finger_array)
        print(finger_combinations.get(finger_key, "Unknown combination"))
        return finger_combinations.get(finger_key, "Unknown combination")

    def handle_request(self, service_name, msg):
        if service_name == 'spawn':
            self.holder = Int16()
        elif service_name == 'kill':
            pass
        elif service_name == '/teleport':
            self.turtle.teleport_turtle(msg)
            print("POS")
        elif service_name == 'spin':
            self.holder = Pos()

    def new(self):
        self.turtle = TurtleSimControl()

def main(args=None):
    rclpy.init(args=args)
    manosManager = Manos_Manager()
    manosManager.new()

    rclpy.spin(manosManager)

if __name__ == '__main__':
    main()