#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist

class Turtlebot(Node):
	def __init__(self):
		super().__init__("turtlebot_controller")
		self.publisher=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
		self.timer=self.create_timer(0.1,self.move_turtle)
	
	def move_turtle(self):
 		msg= Twist()
 		
 		msg.linear.x = 2.0
 		msg.angular.z = 1.0
 		
 		self.publisher.publish(msg)
 		self.get_logger().info("Moving Turtle")
 	
def main():
 	rclpy.init()
 	
 	node=Turtlebot()
 	
 	rclpy.spin(node)
 	
 	node.destroy_node()
 	
 	rclpy.shutdown()
 	
if __name__ == "__main__":	
 	main()		
