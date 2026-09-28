#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class TurtleController(Node):

    def __init__(self):
        super().__init__("turtle_controller")

        # Store current pose
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

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
            0.1,
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

        if self.x < 8.0:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.get_logger().info("Moving Forward")
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info("Reached x = 8. Stopping!")

        self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = TurtleController()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
