#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtleSubscribeNode(Node):
	def __init__(self):
		super().__init__("turtle_subscriber")
		self.Pose_subscription=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
		
	def pose_callback(self,msg):
		self.x = msg.x
		self.y = msg.y
		self.theta = msg.theta
		self.get_logger().info(f"X={msg.x:.2f}, Y={msg.y:.2f}, Theta={msg.theta:.2f}")

def main():
	rclpy.init()
	node=TurtleSubscribeNode()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ =="__main__":
	main()
