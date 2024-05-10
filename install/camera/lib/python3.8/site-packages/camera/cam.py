import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraSubscriber(Node):
    def __init__(self):
        super().__init__('camera_subscriber')
        # Declare a parameter for the image topic
        self.declare_parameter('image_topic', '/picarchu/camera/raw')
        # Use the parameter to get the topic name
        image_topic = self.get_parameter('image_topic').get_parameter_value().string_value

        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            image_topic,
            self.image_callback,
            10)
        self.get_logger().info(f"Subscribing to {image_topic}")
        self.subscription  # prevent unused variable warning

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            self.get_logger().error(f'Could not convert ROS Image to OpenCV: {e}')
            return

        cv2.imshow("Camera Image", cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    camera_subscriber = CameraSubscriber()
    rclpy.spin(camera_subscriber)
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
