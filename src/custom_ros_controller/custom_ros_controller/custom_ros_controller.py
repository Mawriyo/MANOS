import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, Spawn, Kill
from turtlesim.msg import Pose as TPose #This line caused an unessasary amount of frustration
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from custom_msg.msg import ListString, Pos, FourPointRect
from std_msgs.msg import Int16,String

class TurtleSimControl(Node):
    def __init__(self, namespace='turtle1'):
        super().__init__('turtle_sim_control')
        self.namespace = namespace
        self.namespace = "turtle1"
        self.filtered_service_list = []
        self.servicess = []
        self.screenDiff =  FourPointRect()
        self.screenDiff.xmin = float(0)
        self.screenDiff.ymin = float(0)
        self.screenDiff.xmax = float(480)
        self.screenDiff.ymax = float(640)
        self.temp = ListString()
        self.qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)
        
        # self.velocity_publisher = self.create_publisher(Twist, f'/{namespace}/cmd_vel', self.qos_profile)
        self.teleport_client = self.create_client(TeleportAbsolute, f'/{self.namespace}/teleport_absolute')
        self.spawn_client = self.create_client(Spawn, 'spawn')
        self.kill_client = self.create_client(Kill, 'kill')
        self.create_subscription(FourPointRect, "/MANOS/WorkSpace", self.setScreenDifferential ,self.qos_profile)

        #Input Keywords for services here... 
        #additionally HOST_LISTENER provides a list of services that returns a list of services from outside systems.
        # IF you dont know all the services you can work with Just ros2 topic echo /MANOS/ServiceDetector.
        # this also will filter out all the MANOS services. The keyword method is here so you DONT have 
        #to implement all services when you are just looking to implement a few 
        
        self.keywords = ['/clear', '/kill', '/reset', '/turtle_selection', '/follow_me', "/spin"]
        self.spawned_turtles = [] 
        self.service_publisher = self.create_publisher(ListString, "/MANOS/Services",self.qos_profile)
        self.temp.data = self.keywords
        print("before")
        self.service_publisher.publish(self.temp)
        print("after")

        self.servicetimer = self.create_timer(1, self.publish_services)

    def publish_services(self):
        print("In here")

    def setScreenDifferential(self,msg):
        self.screenDiff.xmin = msg.xmin 
        self.screenDiff.ymin = msg.ymin 
        self.screenDiff.xmax = msg.xmax 
        self.screenDiff.ymax = msg.ymax 
    def hear(self,type, name):
        self.create_subscription(type, name, self.teleport_turtle, self.qos_profile)


    def teleport_turtle(self, msg):
            scale_x = (self.screenDiff.xmax - self.screenDiff.xmin) / self.screenDiff.xmax
            scale_y = (self.screenDiff.ymax - self.screenDiff.ymin) / self.screenDiff.ymax
            print(str(scale_x))
            print(str(scale_y)
         # Adjust turtle position within the scaled rectangle
            teleport_request = TeleportAbsolute.Request()
            teleport_request.x = ((msg.x - self.screenDiff.xmin) / scale_x) 
            teleport_request.y = ((msg.y - self.screenDiff.ymin) / scale_y) 
            self.teleport_client.call_async(teleport_request)

    def rotateTurtle(self, msg):
        request = TeleportAbsolute.Request()
        request.x = self.pose.x
        request.y = self.pose.y
        request.theta = self.calculate_theta(10-(msg.x / self.screenDiff.y) * 10, 10 - (msg.y / self.screenDiff.x) * 10)  # Invert the y-coordinate
        self.teleport_client.call_async(request)

    def calculate_theta(self, x, y):
        # Calculate the angle (theta) based on the finger position
        current_x = self.pose.x
        current_y = self.pose.y 
        delta_x = x - current_x
        delta_y = y - current_y

        # Calculate the angle using arctangent (in radians)
        theta = math.atan2(delta_y, delta_x)

        return theta

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return math.sqrt(math.pow((goal_pose.position.x - self.pose.x), 2) +
                    math.pow((goal_pose.position.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return math.atan2(goal_pose.position.y - self.pose.y, goal_pose.position.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self,msg):
        """Moves the turtle to the goal."""
        goal_pose = TPose()
        goal_pose.position.x = (msg.x/ 640) * 10
        goal_pose.position.y = (msg.y/480) * 10
        distance_tolerance =.05
        vel_msg = Twist()

        while self.euclidean_distance(goal_pose) >= distance_tolerance:

            # Proportional controller.
            # https://en.wikipedia.org/wiki/Proportional_control

            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.angular.z = self.angular_vel(goal_pose)
            self.velocity_publisher.publish(vel_msg)

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

    def turleSel(self,name):
        if self.namespace == name:
            pass
        else:
            self.namespace = name
            self.destroy_subscription(self.turtlePoseSubNode)
            self.turtlePoseSubNode = self.create_subscription(TPose, '/'+ self.namespace + '/pose', self.update_pose, self.qos_profile)
   
    def turtleSelection(self, msg): 
        val = msg.data
        if val == 1:
           self.turleSel('turtle1')

        elif val == 2:
            if 'turtle2' not in self.spawned_turtles:
                self.spawned_turtles.append('turtle2')
                self.spawn_turtle('turtle2', 5.0, 3.0, 0.0)
            self.turleSel('turtle2')

        elif val == 3:
            if 'turtle3' not in self.spawned_turtles:
               self.spawned_turtles.append('turtle3')
               self.spawn_turtle('turtle3', 1.0, 4.0, 0.0)
            self.turleSel('turtle3')

        elif val == 4 :
            self.namespace = 'turtle4'
            if 'turtle4' not in self.spawned_turtles:
                self.spawned_turtles.append('turtle4')
                self.spawn_turtle('turtle4', 8.0, 8.0, 0.0)
            self.turleSel('turtle4')

        elif val == 5:
            if 'turtle5' not in self.spawned_turtles:
               self.spawned_turtles.append('turtle5')
               self.spawn_turtle('turtle5', 8.0, 5.0, 0.0)
            self.turleSel('turtle5')

        return self.namespace
    
    
    def kill_turtle(self, turtle_id):
        self.spawned_turtles.remove(turtle_id)
        self.temp = Kill.Request()
        self.temp.name = turtle_id
        self.kill_client.call_asyc(self.temp)   

    def test(self,):
        print("hello from turttle")

    def spawn_turtle(self, name, x, y, theta):
        request = Spawn.Request()
        request.name = name
        request.x = x
        request.y = y
        request.theta = theta
        self.spawnTurtle.call_async(request)

    def update_pose(self, data):
        self.pose = TPose()
        self.pose.x = round(data.x, 4)
        self.pose.y = round(data.y, 4)

    def getServices(self, msg):
        self.servicess = msg.data
        self.filtered_service_list = [(service_name, service_type) for service_name, service_type in self.servicess
                                      if any(keyword in service_name for keyword in self.keywords)]
        
def main(args=None):
    rclpy.init(args=args)
    turtle_control = TurtleSimControl()
    rclpy.spin(turtle_control)

if __name__ == '__main__':
    main()