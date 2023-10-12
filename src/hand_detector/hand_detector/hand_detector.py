import rclpy
import cv2
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from rclpy.node import Node
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
from cvzone import HandTrackingModule
from sensor_msgs.msg import Image
from std_msgs.msg import Int16
from cvzone import HandTrackingModule
import time
from custom_msg.msg import ListString, Pos
class Hand_Detector(Node):

    def __init__(self):
        super().__init__('hand_detector_subscriber')
        self.br = CvBridge()
        self.lhand_fingers_up_publisher =  self.create_publisher(Int16, '/MANOS/Left_Hand/fingers_up', 5) #Records the amount of fingers up on the left hand... Datatructure: array[5] 
        self.lhand_fingers_publisher =  self.create_publisher(ListString, '/MANOS/Left_Hand/fingers', 5) #Records the amount of fingers up on the Right hand... Datatructure: array[5] 
      
        self.lhand_publisher = self.create_publisher(ListString, '/MANOS/Left_Hand', 5)
        self.lhand_thumb_publisher = self.create_publisher(Pos, '/MANOS/Left_Hand/Thumb_pos', 5)
        self.lhand_pointer_publisher = self.create_publisher(Pos, '/MANOS/Left_Hand/Pointer_pos', 5)
        self.lhand_middle_publisher = self.create_publisher(Pos, '/MANOS/Left_Hand/Middle_pos', 5)
        self.lhand_ring_publisher = self.create_publisher(Pos, '/MANOS/Left_Hand/Ring_pos', 5)
        self.lhand_pinky_publisher = self.create_publisher(Pos, '/MANOS/Left_Hand/Pinky_pos', 5)
        self.hand_pose_image = self.create_publisher(Image, '/MANOS/camera/hand_pos', qos_profile)


        self.rhand_fingers_up_publisher =  self.create_publisher(Int16, '/MANOS/Right_Hand/fingers_up', 5) #Records the amount of fingers up on the Right hand... Datatructure: array[5] 
        self.rhand_fingers_publisher =  self.create_publisher(ListString, '/MANOS/Right_Hand/fingers', 5) #Records the amount of fingers up on the Right hand... Datatructure: array[5] 
     
        self.rhand_publisher = self.create_publisher(ListString, '/MANOS/Right_Hand', 5) #Records the right hand pose within the frame... Datatructure: array[26]
        self.rhand_thumb_publisher = self.create_publisher(Pos, '/MANOS/Right_Hand/Thumb_pos', 5)
        self.rhand_pointer_publisher = self.create_publisher(Pos, '/MANOS/Right_Hand/Pointer_pos', 5)
        self.rhand_middle_publisher = self.create_publisher(Pos, '/MANOS/Right_Hand/Middle_pos', 5)
        self.rhand_ring_publisher = self.create_publisher(Pos, '/MANOS/Right_Hand/Ring_pos', 5)
        self.rhand_pinky_publisher = self.create_publisher(Pos, '/MANOS/Right_Hand/Pinky_pos', 5)
        self.hand_pose_image = self.create_publisher(Image, '/MANOS/camera/hand_pos', qos_profile)


        qos_profile = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT,
                                 durability=DurabilityPolicy.VOLATILE,
                                 history=HistoryPolicy.KEEP_LAST,
                                 depth=1)
        self.raw_image_subscription = self.create_subscription(Image, '/MANOS/camera/raw_image', self.imagedecoder_callback, qos_profile)

        #Records the left hand pose within the frame... Datatructure: array[26]
        self.detector =  HandTrackingModule.HandDetector(detectionCon=0.73, maxHands=2)



    def imagedecoder_callback(self, data):
        msg = Int16()
        fingermsg = ListString()
        current_frame = self.br.imgmsg_to_cv2(data)
        
        hands, img = self.detector.findHands(current_frame)
        
        print("cvzone" + str(type(self.br.cv2_to_imgmsg(current_frame))))

         #only publish images.... not the other thing... 
        # if not (type(self.br.cv2_to_imgmsg(img)) == "numpy.ndarray"):
        self.hand_pose_image.publish(self.br.cv2_to_imgmsg(img))


        if len(hands) == 1:
            hand1=hands[0]
            lmList1 = hand1["lmList"]
            digits=self.lmList_convert(lmList1)
            msg.data = sum(self.detector.fingersUp(hand1))
            fingermsg.data = self.detector.fingersUp(hand1)

            if (hand1["type"]=="Right"):
                self.rhand_fingers_up_publisher.publish(msg)

                self.rhand_thumb_publisher.publish(self.pos_message(digits[0]))
                self.rhand_pointer_publisher.publish(self.pos_message(digits[1]))
                self.rhand_middle_publisher.publish(self.pos_message(digits[2]))
                self.rhand_ring_publisher.publish(self.pos_message(digits[3]))
                self.rhand_pinky_publisher.publish(self.pos_message(digits[4]))
                return

            if (hand1["type"]=="Left"):
                self.lhand_fingers_up_publisher.publish(msg)
                self.lhand_thumb_publisher.publish(self.pos_message(self.thumb))
                self.lhand_pointer_publisher.publish(self.pos_message(self.pointer))
                self.lhand_middle_publisher.publish(self.pos_message(self.middle))
                self.lhand_ring_publisher.publish(self.pos_message(self.ring))
                self.lhand_pinky_publisher.publish(self.pos_message(self.pinky))
                return

        elif len(hands) == 2:
            hand1=hands[0]
            hand2=hands[1]

            #8=index 12 = middle finger 16=ring 20=pink
            
            lmList1 = hand1["lmList"]
            lmList2 = hand2["lmList"]

            #(lmList1[4][0:2]) #returns XY I am not sure what the last value is in the list...

            if (hand1["type"]=="Right"):
                
                msg.data=sum(self.detector.fingersUp(hand1))
                rdigits=self.lmList_convert(lmList1)
                self.rhand_fingers_up_publisher.publish(msg)
                self.rhand_thumb_publisher.publish(self.pos_message(rdigits[0]))
                self.rhand_pointer_publisher.publish(self.pos_message(rdigits[1]))
                self.rhand_middle_publisher.publish(self.pos_message(rdigits[2]))
                self.rhand_ring_publisher.publish(self.pos_message(rdigits[3]))
                self.rhand_pinky_publisher.publish(self.pos_message(rdigits[4]))

                msg.data=sum(self.detector.fingersUp(hand2))
                ldigits=self.lmList_convert(lmList2)
                self.lhand_fingers_up_publisher.publish(msg)
                self.lhand_thumb_publisher.publish(self.pos_message(ldigits[0]))
                self.lhand_pointer_publisher.publish(self.pos_message(ldigits[1]))
                self.lhand_middle_publisher.publish(self.pos_message(ldigits[2]))
                self.lhand_ring_publisher.publish(self.pos_message(ldigits[3]))
                self.lhand_pinky_publisher.publish(self.pos_message(ldigits[4]))

            if (hand1["type"]=="Left"):
                msg.data=sum(self.detector.fingersUp(hand1))
                ldigits=self.lmList_convert(lmList1)

                self.lhand_fingers_up_publisher.publish(msg)
                self.lhand_thumb_publisher.publish(self.pos_message(ldigits[0]))
                self.lhand_pointer_publisher.publish(self.pos_message(ldigits[1]))
                self.lhand_middle_publisher.publish(self.pos_message(ldigits[2]))
                self.lhand_ring_publisher.publish(self.pos_message(ldigits[3]))
                self.lhand_pinky_publisher.publish(self.pos_message(ldigits[4]))
               
                msg.data=sum(self.detector.fingersUp(hand2))
                rdigits=self.lmList_convert(lmList2)
                self.rhand_fingers_up_publisher.publish(msg)
                self.rhand_thumb_publisher.publish(self.pos_message(rdigits[0]))
                self.rhand_pointer_publisher.publish(self.pos_message(rdigits[1]))
                self.rhand_middle_publisher.publish(self.pos_message(rdigits[2]))
                self.rhand_ring_publisher.publish(self.pos_message(rdigits[3]))
                self.rhand_pinky_publisher.publish(self.pos_message(rdigits[4]))

#Sacrificing memory for readability here... 
    def lmList_convert(self, lmlist):
        digits = []
        self.thumb = lmlist[4][0:2]
        self.pointer = lmlist[8][0:2]
        self.middle = lmlist[12][0:2]
        self.ring = lmlist[16][0:2]
        self.pinky = lmlist[20][0:2]

        digits.append(self.thumb)
        digits.append(self.pointer)
        digits.append(self.middle)
        digits.append(self.ring)
        digits.append(self.pinky)

        return digits
    
    def pos_message(self, digit):
        pos = Pos()
        pos.x = float(digit[0])
        pos.y = float(digit[1])
        return pos
    
        
def main(args=None):
    rclpy.init(args=args)
    hand_detector_subscriber = Hand_Detector()
    rclpy.spin(hand_detector_subscriber)

if __name__ == '__main__':
    main()
