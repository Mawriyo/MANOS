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

        self.qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)
        

        self.bindingSelection = self.create_subscription(String, "/MANOS/binding", self.checkBindingSelection, self.qos_profile)
        self.menuSelectionSub = self.create_subscription(String, "/MANOS/menuSelection", self.checkMenuSelection, self.qos_profile)
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

    def handle_pointer_pos(self, msg):
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