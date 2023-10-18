import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, Spawn
from turtlesim.msg import Pose as TPose #This line caused an unessasary amount of frustration
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from custom_msg.msg import ListString, Pos

class TurtleSimControl(Node):
    def __init__(self, namespace='turtle1'):
        super().__init__('turtle_sim_control')
        self.namespace = namespace
        self.qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)
        self.velocity_publisher = self.create_publisher(Twist, f'/{namespace}/cmd_vel', self.qos_profile)
        self.teleport_client = self.create_client(TeleportAbsolute, f'/{namespace}/teleport_absolute')
        self.spawn_client = self.create_client(Spawn, 'spawn')
        self.teleportNode = self.create_subscription(TPose, '/'+ self.namespace + '/pose', self.update_pose, self.qos_profile)
        self.serviceList = self.create_subscription(ListString, "/MANOS/ServiceDetector",self.getServices, self.qos_profile)
        self.keywords = [] #Input Keywords for services here
        self.spawned_turtles = []  

    def move_turtle_to_goal(self, x, y):
        twist_msg = Twist()
        goal_x, goal_y = x, y
        distance_tolerance = 0.05

        while self.euclidean_distance(goal_x, goal_y) >= distance_tolerance:
            linear_vel = self.linear_velocity(goal_x, goal_y)
            angular_vel = self.angular_velocity(goal_x, goal_y)
            twist_msg.linear.x = linear_vel
            twist_msg.angular.z = angular_vel
            self.velocity_publisher.publish(twist_msg)

        # Stop the turtle after reaching the goal
        twist_msg.linear.x = 0
        twist_msg.angular.z = 0
        self.velocity_publisher.publish(twist_msg)

    def teleport_turtle(self, msg):
        teleport_request = TeleportAbsolute.Request()
        teleport_request.x = 10- (msg.x / 640) * 10
        teleport_request.y = 10 - (msg.y / 480) * 10  # Invert the y-coordinate
        teleport_request.theta = 0.0  # Ensure that the turtle does not change its orientation
        self.teleport_service.call_async(teleport_request)

    def rotateTurtle(self, msg):
        request = TeleportAbsolute.Request()
        request.x = self.pose.x
        request.y = self.pose.y
        request.theta = self.calculate_theta(10-(msg.x / 640) * 10, 10 - (msg.y / 480) * 10)  # Invert the y-coordinate
        self.teleport_service.call_async(request)

    def euclidean_distance(self, goal_x, goal_y):
        current_x = 0.0  # Get the current turtle's x-position here
        current_y = 0.0  # Get the current turtle's y-position here
        return ((goal_x - current_x) ** 2 + (goal_y - current_y) ** 2) ** 0.5

    def linear_velocity(self, goal_x, goal_y, constant=1.5):
        return constant * self.euclidean_distance(goal_x, goal_y)

    def angular_velocity(self, goal_x, goal_y, constant=6):
        return constant * (self.steering_angle(goal_x, goal_y) - 0.0)

    def steering_angle(self, goal_x, goal_y):
        current_x = self.pose.x # Get the current turtle's x-position here
        current_y = self.pose.y  # Get the current turtle's y-position here
        return 0.0  # Calculate the steering angle
    def kill_turtle(self, turtle_id):
        if turtle_id in self.spawned_turtles:
            self.node.destroy_subscription(old_subscription)
            self.spawned_turtles.remove(turtle_id)
            
    def turtleSelection(self, msg):
        val = msg.data
        if val == 1:
            self.namespace = 'turtle1'

        elif val == 2:
            self.namespace = 'turtle2'
            if 'turtle2' not in self.spawned_turtles:
                self.spawned_turtles.append('turtle2')
                self.spawn_turtle('turtle2', 5.0, 3.0, 0.0)
        elif val == 3:
            self.namespace = 'turtle3'
            if 'turtle3' not in self.spawned_turtles:
               self.spawned_turtles.append('turtle3')
               self.spawn_turtle('turtle3', 1.0, 4.0, 0.0)
        elif val == 4 :
            self.namespace = 'turtle4'
            if 'turtle4' not in self.spawned_turtles:
                self.spawned_turtles.append('turtle4')
                self.spawn_turtle('turtle4', 8.0, 8.0, 0.0)
        elif val == 5:
            self.namespace = 'turtle5'
            if 'turtle5' not in self.spawned_turtles:
               self.spawned_turtles.append('turtle5')
               self.spawn_turtle('turtle5', 8.0, 5.0, 0.0)
        return self.namespace
    
    def kill_turtle_by_id(self, turtle_id):
        if turtle_id == 1:
            self.kill_turtle('turtle1')
        elif turtle_id == 2:
            self.kill_turtle('turtle2')
        elif turtle_id == 3:
            self.kill_turtle('turtle3')
        elif turtle_id == 4:
            self.kill_turtle('turtle4')
        elif turtle_id == 5:
            self.kill_turtle('turtle5')

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

    def getServices(self,data):
        self.services = data
        self.filtered_service_list = [(service_name, service_type) for service_name, service_type in  self.services
                                if any(keyword in service_name for keyword in self.keywords)]

        return self.filtered_service_list
    
def main(args=None):
    rclpy.init(args=args)
    turtle_control = TurtleSimControl()
    # Use the methods of TurtleSimControl to control the turtle
    rclpy.spin(turtle_control)
    rclpy.shutdown()

if __name__ == '__main__':
    main()