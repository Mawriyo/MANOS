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



        qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)

        # self.topic_subscriber = self.create_subscription(ListString, '/MANOS/TopicDetector', qos_profile)
        self.service_publisher = self.create_publisher(ListString, '/MANOS/Manager/Services', qos_profile)
        self.topic_publisher = self.create_publisher(ListString, '/MANOS/Topics', qos_profile)

        self.topictimer = self.create_timer(timer_period, self.filter_and_store_topics)
        self.servicetimer = self.create_timer(timer_period, self.filter_and_store_services)

    def filter_and_store_topics(self):
        topic_names_and_types = self.get_topic_names_and_types()
        
        filtered_topic_names_and_types = [(topic_name, topic_type) for topic_name, topic_type in topic_names_and_types
                                          if not any(keyword in topic_name for keyword in ["camera_publisher", "parameter", "topic_names_node", "host_detector_subscriber", "castelet_node"])]

        self.ros_topic_list = [topic_name for topic_name, _ in filtered_topic_names_and_types]
        self.publish_topics(self.ros_topic_list)

    def publish_topics(self, topic_list):
        list_string_msg = ListString()
        list_string_msg.data = topic_list
        #print("Publishing topics" + str(list_string_msg))

        self.topic_publisher.publish(list_string_msg)


    def filter_and_store_services(self):
        Service = ListString()
        self.keywords = ['/clear', '/kill', '/reset', '/teleport', "/spin","/select","/servo_control","/servo_select"]
        Service.data = self.keywords
        self.spawned_turtles = [] 
        self.service_publisher.publish(Service)

    def publish_services(self, service_list ):
        list_string_msg = ListString()
        list_string_msg.data = service_list
        print("Publishing services" + str(list_string_msg))
        self.service_publisher.publish(list_string_msg)


def main(args=None):
    rclpy.init(args=args)
    host_detector = Host_Detector()
    rclpy.spin(host_detector)



if __name__ == '__main__':
    main()
