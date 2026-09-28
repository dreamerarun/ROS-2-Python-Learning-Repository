#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
class MultiRobot_Publisher(Node):
	def __init__(self):
		super().__init__("multirobot")	
		self.publisher1 = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
		self.publisher2 = self.create_publisher(Twist,"/turtle2/cmd_vel",10)
		self.timer = self.create_timer(0.1,self.move_turtle)
		
	def move_turtle(self):
			msg1=Twist()
			msg2=Twist()
			msg1.linear.x = 2.0
			msg1.angular.z = 0.0
			msg2.linear.x = 3.0
			msg2.angular.z = 0.0
			self.get_logger().info(f"Turtle1={msg1.linear.x}, Turtle2={msg2.linear.x}")
			self.publisher1.publish(msg1)
			self.publisher2.publish(msg2)

def main(args=None):
	rclpy.init(args=args)
	node = MultiRobot_Publisher()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()

if __name__ == "__main__":
	main()

