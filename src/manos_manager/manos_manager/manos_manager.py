
from custom_ros_controller.custom_ros_controller import TurtleSimControl
from custom_ros_controller.picarchu_controller import PiCarChuControl
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from custom_msg.msg import ListString,Pos
from std_msgs.msg import Int16, String
from functools import partial


#todo: ADD FEEDBACK FOR GUI... MAYBE PUBLISH TO /MANOS/CASTELET/NOTIFCATION AND MANOS/CASTELET/UPDATEGUI

class ManosManager(Node):
    def __init__(self):
        super().__init__('manos_manager')
        self.current_topic = ""
        self.menu_item = ""
        self.finger_array = []
        self.fingersup_array = []
        self.finger_combinations = {
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
        self.qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                      durability=DurabilityPolicy.VOLATILE,
                                      history=HistoryPolicy.KEEP_LAST,
                                      depth=1)
        self.fingerup_sub = self.create_subscription(ListString,"/MANOS/Left_Hand/fingers",self.fingersup, self.qos_profile)
        self.binding_selection_sub = self.create_subscription(String, "/MANOS/Manager/TopicSelection", self.check_menu_selection, self.qos_profile)
        self.fingers_array_sub = self.create_subscription(String, "/MANOS/Manager/FingerSelection", self.finger_selection, self.qos_profile)
        self.hand_selection_sub = self.create_subscription(String, "/MANOS/Manager/HandSelection", self.hand_selection, self.qos_profile)
        self.type_sub = self.create_subscription(String, "/MANOS/Manager/TypeSelection", self.sub_creation, self.qos_profile)
        self.turtle_demo_sub = self.create_subscription(Bool, "TurtleDemo", self.sub_creation, self.qos_profile)

    def get_finger_name(self, finger_array):
        finger_key = str(finger_array)
        print (finger_key)
        print("Available keys:")
        for key in self.finger_combinations.keys():
            print(f"'{key}'")
        temp = self.finger_combinations[finger_key]
        print (temp)
        return temp

    def fingersup(self, msg):
        self.fingersup_array = msg.data

    def change_callback(self, sub_key, topic_type, topic, function):
        if sub_key in self.subscriptions:
            old_subscription = self.subscriptions[sub_key]
            if old_subscription:
                self.destroy_subscription(old_subscription)
        new_subscription = self.create_subscription(topic_type, topic, function, self.qos_profile)
        self.subscriptions[sub_key] = new_subscription

    def check_menu_selection(self, msg):
        self.menu_item = msg.data
        print(str(self.menu_item))

    def finger_selection(self, msg):
        self.finger_array = msg.data


    def hand_selection(self, msg):
        self.current_hand = msg.data
        
    def handle_request(self, service_name, msg):

        if service_name == '/spin': 
            print("Executing: spin")
            return
            self.turtle.rotate_turtle(msg)
        elif service_name == '/teleport':
            print("Executing: teleport")
            self.turtle.teleport_turtle(msg)
        elif service_name == '/select':
            print("Executing: select")
            self.turtle.turtle_selection(msg)
        elif service_name == '/kill':
            print("Executing: kill")
            self.turtle.turtle_removal(msg)
        elif service_name == '/servo_select':
            self.servo_controller.select_servo(msg)
        elif service_name == '/servo_control':
            self.servo_controller.send_servo_command(msg)
        else:
            pass
        
        
    def new(self):
        self.turtle = TurtleSimControl() 
        self.servo_controller =PiCarChuControl()

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
