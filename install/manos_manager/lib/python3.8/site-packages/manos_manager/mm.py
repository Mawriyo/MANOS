import math
from TurtleSimControl import TurtleSimControl
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, Spawn, Kill
from turtlesim.msg import Pose as TPose #This line caused an unessasary amount of frustration
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from custom_msg.msg import ListString, Int16

class Manos_Manager(Node):
    def __init__(self, ):
        super().__init__('manos_manager')
        self.qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)
        

        self.bindingSelection = self.create_subscription(ListString, "/MANOS/Bindings/binding", self.checkBindingSelection, self.qos_profile)
        self.menuSelectionSub = self.create_subscription(Int16, "/MANOS/Bindings/menuSelection", self.checkMenuSelection, self.qos_profile)
        self.turtleSim = TurtleSimControl()
        
    def checkMenuSelection(self, msg):
        self.menuItem=msg.data

    def checkBindingSelection(self, msg):
        self.binding=msg.data
        
    
    def test(self):
        self.subscriber = self.create_node(Pos, self.menuItem, TurtleSimControl.teleport_turtle,self.qos_profile)
        
def main(args=None):
    rclpy.init(args=args)
    manosManager = Manos_Manager()
    rclpy.spin(manosManager)

if __name__ == '__main__':
    main()