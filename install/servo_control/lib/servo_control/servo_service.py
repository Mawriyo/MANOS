#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from custom_msg.srv import SetServo


class ServoServiceNode(Node):
    def __init__(self):
        super().__init__('servo_service_node')
        self.client = self.create_client(SetServo, 'set_servo')

    def send_servo_command(self, msg):
        request = SetServo.Request()
        request.id = msg.id
        request.position = msg.position
        self.future = self.client.call_async(request)
        return self.future

def main(args=None):
    rclpy.init(args=args)
    servo_service_node = ServoServiceNode()
    rclpy.spin(servo_service_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
