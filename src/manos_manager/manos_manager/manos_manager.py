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


#todo: ADD FEEDBACK FOR GUI... MAYBE PUBLISH TO /MANOS/CASTELET/NOTIFCATION AND MANOS/CASTELET/UPDATEGUI
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
class ManosManager(Node):
    def __init__(self):
        super().__init__('manos_manager')
        self.current_topic = ""
        self.menu_item = ""
        self.finger_array = []
        self.finger_combinations_dict = {}
        self.qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                      durability=DurabilityPolicy.VOLATILE,
                                      history=HistoryPolicy.KEEP_LAST,
                                      depth=1)

        self.binding_selection_sub = self.create_subscription(String, "/MANOS/Manager/TopicSelection", self.check_menu_selection, self.qos_profile)
        self.fingers_array_sub = self.create_subscription(String, "/MANOS/Manager/FingerSelection", self.finger_selection, self.qos_profile)
        self.hand_selection_sub = self.create_subscription(String, "/MANOS/Manager/HandSelection", self.hand_selection, self.qos_profile)
        self.type_sub = self.create_subscription(String, "/MANOS/Manager/TypeSelection", self.sub_creation, self.qos_profile)

    def change_callback(self, sub_key, topic_type, topic, function):
        if sub_key in self.subscriptions:
            old_subscription = self.subscriptions[sub_key]
            if old_subscription:
                self.destroy_subscription(old_subscription)
        new_subscription = self.create_subscription(topic_type, topic, function, self.qos_profile)
        self.subscriptions[sub_key] = new_subscription

    def check_menu_selection(self, msg):
        self.menu_item = msg.data
        print(str(self.menu_item)) #/TELEPORT

    def finger_selection(self, msg):
        self.finger_array = msg.data
        if self.finger_array in self.finger_combinations_dict:
            del self.finger_combinations_dict[self.finger_array]
        else:
            self.finger_combinations_dict[self.finger_array] = True

    def get_finger_name(self, finger_array):
        finger_key = str(finger_array)
        return finger_combinations.get(finger_key, "Unknown combination")

    def hand_selection(self, msg):
        self.current_hand = msg.data
        print(str(self.current_hand) + "test")

    def handle_request(self, service_name, msg):
        if service_name == '/select':
            self.turtle.turtle_selection(msg)
        elif service_name == '/kill':
            self.turtle.turtle_removal(msg)
        elif service_name == '/teleport':
            self.turtle.teleport_turtle(msg)
        elif service_name == '/spin':
            self.turtle.rotate_turtle(msg)

    def new(self):
        self.turtle = TurtleSimControl()

    def sub_creation(self, msg):
        if msg.data == 'Pos':
            string = self.current_hand + self.get_finger_name(self.finger_array)
            self.create_subscription(Pos(), string, partial(self.handle_request, self.menu_item), self.qos_profile)
        elif msg.data == "FingersUp":
            string = self.current_hand + "fingers_up"
            self.create_subscription(Int16(), string, partial(self.handle_request, self.menu_item), self.qos_profile)

def main(args=None):
    rclpy.init(args=args)
    manos_manager = ManosManager()
    manos_manager.new()

    rclpy.spin(manos_manager)

if __name__ == '__main__':
    main()