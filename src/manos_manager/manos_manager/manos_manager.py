import math
import threading
from custom_ros_controller.custom_ros_controller import TurtleSimControl
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, Spawn, Kill
from turtlesim.msg import Pose as TPose #This line caused an unessasary amount of frustration
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from custom_msg.msg import ListString,Pos
from std_msgs.msg import Int16, String


class Manos_Manager(Node):
    def __init__(self):
        super().__init__('manos_manager')
        self.menuItem = ""
        self.currentArray =[]
        self.fingersUp = 0 #TODO test to see if subscribing to fingersup vs adding all items in current array is faster/more efficient.
        self.finger_combinations_dict = {}
        self.qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)

        self.bindingSelection = self.create_subscription(String, "/MANOS/binding", self.checkBindingSelection, self.qos_profile)
        self.menuSelectionSub = self.create_subscription(String, "/MANOS/menuSelection", self.checkMenuSelection, self.qos_profile)
        self.fingersArraySub = self.create_subscription(ListString, "/MANOS/menuSelection", self.getFingersArray, self.qos_profile)

        self.temp = False
        # self.turtleSelection = self.turtle.namespace
        # t1= threading.Thread(target=self.new)
        # t1.start()
        # self.new()

    def checkMenuSelection(self, msg):
        self.menuItem=msg.data
        print( self.menuItem) #//MANOS/Right_Hand/Pointer_pos
        print( self.binding) #/turtle1/teleport_absolute

        print(f"{type(self.menuItem)} type")
        # self.turtle.teleport_client.
        self.pointer_pos_sub = self.create_subscription(Pos,  self.menuItem, self.handle_pointer_pos, self.qos_profile)
                #check out make a dictionarry that keeps track what functions are bound to a corisponding combination of fingers... 
                # [0,1,1,0,0] means pointer and middle are up... if the array has an associated function bound remove it and rebind it...

    def getFingersArray(self,msg):
        self.currentArray = msg.data
        print(self.currentArray)
        finger_states = [int(finger_state) for finger_state in self.currentArray]
        # self.fingersUp = sum(finger_states) TODO TEST
        finger_combination = tuple(finger_states)  # Convert list to tuple for dictionary key
        if finger_combination in self.finger_combinations_dict:
            action = self.finger_combinations_dict[finger_combination]
            action()            
    def handle_pointer_pos(self, msg):
        print(msg)
        self.turtle.teleport_turtle(msg)

    def checkBindingSelection(self, msg):
        self.binding=msg.data #/MANOS/Left_Hand/Pointer_pos WHICH UPON SUBSCRIBING YOU GET A pos() LIKE x: 535.0 y: 334.0




    def test(self):
        # self.turtle.test()
        while not self.temp:
            try:
                self.turtle.hear(Pos, self.menuItem)
                # self.fingersUP = self.create_subscription(Pos, "/MANOS/Left_Hand/Pointer_pos", self.turtle.teleport_turtle ,self.qos_profile)
            except:
                pass

    def new(self):
        self.turtle = TurtleSimControl()

        # thread2 = threading.Thread(target=rclpy.spin, args=(  self.turtle,), daemon=True)
        # self.turtle.test()

def main(args=None):
    rclpy.init(args=args)
    manosManager = Manos_Manager()
    manosManager.new()

    rclpy.spin(manosManager)

if __name__ == '__main__':
    main()