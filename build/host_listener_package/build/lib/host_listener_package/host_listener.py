#from std_msg.msg import String
import rclpy
from rclpy.node import Node
from custom_msg.msg import ListString
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

class Host_Detector(Node):

    def __init__(self):
        super().__init__('host_detector')
        self.ros_topic_list = []
        self.old_length=0 
        timer_period = 1  
        self.timer = self.create_timer(timer_period, self.get_topic_names_and_types)
        self.node = rclpy.create_node('topic_names_node')
        qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)
        self.topic_publisher = self.node.create_publisher(ListString, '/MANOS/TopicDetector', qos_profile)
        self.service_publisher = self.node.create_publisher(ListString, '/MANOS/ServiceDetector', qos_profile)



    def get_topic_names_and_types(self):
        topic_names_and_types = self.node.get_topic_names_and_types()
        service_list = self.node.get_service_names_and_types()
        
        # Filter out unwanted topics
        filtered_topic_names_and_types = [(topic_name, topic_type) for topic_name, topic_type in topic_names_and_types
                                        if not any(keyword in topic_name for keyword in ["camera_publisher", "parameter", "topic_names_node", "host_detector_subscriber","castelet_node"])]

        # Filter out unwanted services
        filtered_service_list = [(service_name, service_type) for service_name, service_type in service_list
                                if not any(keyword in service_name for keyword in ["camera_publisher", "parameter", "topic_names_node", "host_detector_subscriber","castelet_node"])]

        self.ros_topic_list = [topic_name for topic_name, _ in filtered_topic_names_and_types]
        self.ros_service_list = [service_name for service_name, _ in filtered_service_list]
        
        list_string_msg = ListString()
        list_string_msg.data = self.ros_topic_list
        
        if len(self.ros_topic_list) != self.old_length:
            self.old_length = len(self.ros_topic_list)
            self.topic_publisher.publish(list_string_msg)
            
        list_string_msg.data = self.ros_service_list
        self.service_publisher.publish(list_string_msg)

def main(args=None):
    rclpy.init(args=args)
    host_detector = Host_Detector()
    rclpy.spin(host_detector)



if __name__ == '__main__':
    main()
