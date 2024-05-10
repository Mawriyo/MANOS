import cv2
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images



class Camera_Publisher(Node):

    def __init__(self):
        super().__init__('camera_publisher')
        #camera_arg = self.get_parameter('camera_arg').get_parameter_value().string_value
        self.cam= cv2.VideoCapture(0)
        self.br = CvBridge()
        self.raw_image_publisher = self.create_publisher(Image, '/MANOS/camera/raw', 60)
        timer_period = .01 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
    def timer_callback(self):
        ret, frame = self.cam.read()
        if ret == True:
          print("yes")
          self.raw_image_publisher.publish(self.br.cv2_to_imgmsg(frame))

def main(args=None):
    rclpy.init(args=args)
    camera_publisher = Camera_Publisher()
    rclpy.spin(camera_publisher)

if __name__ == '__main__':
    main()
