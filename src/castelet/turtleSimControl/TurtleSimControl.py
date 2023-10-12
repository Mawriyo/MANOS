import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, Spawn

class TurtleSimControl(Node):
    def __init__(self, namespace='turtle1'):
        super().__init__('turtle_sim_control')
        self.namespace = namespace
        self.velocity_publisher = self.create_publisher(Twist, f'/{namespace}/cmd_vel', 2)
        self.teleport_client = self.create_client(TeleportAbsolute, f'/{namespace}/teleport_absolute')
        self.spawn_client = self.create_client(Spawn, 'spawn')

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

    def teleport_turtle(self, x, y):
        request = TeleportAbsolute.Request()
        request.x = x
        request.y = y
        request.theta = 0.0
        self.teleport_client.call(request)

    def spawn_additional_turtle(self, name, x, y):
        request = Spawn.Request()
        request.name = name
        request.x = x
        request.y = y
        request.theta = 0.0
        self.spawn_client.call(request)

    def euclidean_distance(self, goal_x, goal_y):
        current_x = 0.0  # Get the current turtle's x-position here
        current_y = 0.0  # Get the current turtle's y-position here
        return ((goal_x - current_x) ** 2 + (goal_y - current_y) ** 2) ** 0.5

    def linear_velocity(self, goal_x, goal_y, constant=1.5):
        return constant * self.euclidean_distance(goal_x, goal_y)

    def angular_velocity(self, goal_x, goal_y, constant=6):
        return constant * (self.steering_angle(goal_x, goal_y) - 0.0)

    def steering_angle(self, goal_x, goal_y):
        current_x = 0.0  # Get the current turtle's x-position here
        current_y = 0.0  # Get the current turtle's y-position here
        return 0.0  # Calculate the steering angle

def main(args=None):
    rclpy.init(args=args)
    turtle_control = TurtleSimControl()
    # Use the methods of TurtleSimControl to control the turtle
    rclpy.spin(turtle_control)
    rclpy.shutdown()

if __name__ == '__main__':
    main()