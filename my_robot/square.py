#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleController(Node):

    def __init__(self):
        super().__init__("square_maker")
        # Store current pose
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.start_x = 0.0
        self.start_y = 0.0
        self.start_theta = 0.0
        self.state = "MOVE"
        self.side = 0
        # Publisher
        self.publisher = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )
        # Subscriber
        self.pose_subscription = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.pose_callback,
            10
        )
        # Timer (10 Hz)
        self.timer = self.create_timer(
            0.02,
            self.move_turtle
        )

    def pose_callback(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.theta = msg.theta
        self.get_logger().info(
            f"X={self.x:.2f}, Y={self.y:.2f}, Theta={self.theta:.2f}"
        )

    def move_turtle(self):

        msg = Twist()
        if self.side <= 5:
               if self.state == "MOVE":
                        distance = math.sqrt(
    (self.x - self.start_x)**2 +
    (self.y - self.start_y)**2
)
                        if distance < 2:
                                msg.linear.x = 2.0
                                msg.linear.y = 0.0
                                msg.angular.z = 0.0
                                self.get_logger().info("Moving Forward")
       
                        else:
                                self.state = "TURN"
                                self.start_theta = self.theta
                                self.get_logger().info("moving forward finished")
	    			
               elif self.state == "TURN":
                        angle = abs(math.atan2(
    math.sin(self.theta - self.start_theta),
    math.cos(self.theta - self.start_theta)
))

                        if angle < 1.3:
                                msg.linear.x = 0.0
                                msg.linear.y = 0.0
                                msg.angular.z = 1.257
                                self.get_logger().info("Turning 90 degree")
       
                        else:
                                self.state = "MOVE"
                                self.start_x = self.x
                                self.start_y = self.y
                                self.get_logger().info("turning 90 degree completed")
                                self.side += 1
        else:
                msg.linear.x = 0.0
                msg.linear.y = 0.0
                msg.angular.z = 0.0
                self.get_logger().info("Square achieved. Stopping!")

        self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = TurtleController()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
