#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from custom_msg.srv import SetServo


class PiCarChuControl(Node):
    def __init__(self):
        super().__init__('servo_service_node')
        self.client = self.create_client(SetServo, 'set_servo')
        self.current_servo = 7
        Service = ListString()
        self.keywords = ['/servo_select', '/servo_control,' '/reset','/select']
        Service.data = self.keywords

        
    def select_servo(self, msg):
        self.current_servo = msg.data

    
    def send_servo_command(self, msg):
        request = SetServo.Request()
        request.id = self.current_servo
        request.position = msg.y
        self.future = self.client.call_async(request)
        return self.future
    
    
    def servo_reset(self, msg):
        request = SetServo.Request()
        request.id = self.current_servo
        request.position = msg.y
        self.future = self.client.call_async(request)
        return self.future

def main(args=None):
    rclpy.init(args=args)
    servo_service_node = PiCarChuControl()
    rclpy.spin(servo_service_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
