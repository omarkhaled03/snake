import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
import math
class Joints(Node):
    def __init__(self):
        super().__init__("talker")
        self.joint_1_pub_ = self.create_publisher(Float64MultiArray,'/joints1_controllers/commands',10)
        self.joint_2_pub_ = self.create_publisher(Float64MultiArray,'/joints2_controllers/commands',10)
        self.joint_3_pub_ = self.create_publisher(Float64MultiArray,'/joints3_controllers/commands',10)
        self.joint_4_pub_ = self.create_publisher(Float64MultiArray,'/joints4_controllers/commands',10)
        self.joint_5_pub_ = self.create_publisher(Float64MultiArray,'/joints5_controllers/commands',10)
        self.joint_6_pub_ = self.create_publisher(Float64MultiArray,'/joints6_controllers/commands',10)
        self.joint_7_pub_ = self.create_publisher(Float64MultiArray,'/joints7_controllers/commands',10)
        self.joint_8_pub_ = self.create_publisher(Float64MultiArray,'/joints8_controllers/commands',10)
        self.joint_9_pub_ = self.create_publisher(Float64MultiArray,'/joints9_controllers/commands',10)

        timer_period =  1/20
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0
        self.phase_shift=-30
    def timer_callback(self):
        msg1= Float64MultiArray()
        msg2= Float64MultiArray()
        msg3= Float64MultiArray()
        msg4= Float64MultiArray()
        msg5= Float64MultiArray()
        msg6= Float64MultiArray()
        msg7= Float64MultiArray()
        msg8= Float64MultiArray()
        msg9= Float64MultiArray() 
        msg1.data = [math.sin(self.count)]
        self.joint_1_pub_.publish(msg1)

        msg2.data = [5*math.sin(self.count+1*self.phase_shift)]
        self.joint_2_pub_.publish(msg2)

        msg3.data = [5*math.sin(self.count+2*self.phase_shift)]
        self.joint_3_pub_.publish(msg3)

        msg4.data = [5*math.sin(self.count+3*self.phase_shift)]
        self.joint_4_pub_.publish(msg4)

        msg5.data = [5*math.sin(self.count+4*self.phase_shift)]
        self.joint_5_pub_.publish(msg5)

        msg6.data = [5*math.sin(self.count+5*self.phase_shift)]
        self.joint_6_pub_.publish(msg6)

        msg7.data = [5*math.sin(self.count+6*self.phase_shift)]
        self.joint_7_pub_.publish(msg7)

        msg8.data = [5*math.sin(self.count+7*self.phase_shift)]
        self.joint_8_pub_.publish(msg8)

        msg9.data = [5*math.sin(self.count+8*self.phase_shift)]
        self.joint_9_pub_.publish(msg9)

        self.count +=1
    
    
def main(args=None):
        rclpy.init(args=args)
        Joint = Joints()
        rclpy.spin( Joint)
        rclpy.shutdown()
        Joints.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
        main()
    