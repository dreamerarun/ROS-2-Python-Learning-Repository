#!/usr/bin/env python3

import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class MultiRobot_Sub(Node):

    def __init__(self):
        super().__init__("multirobot")

        self.x1 = 0.0
        self.y1 = 0.0
        self.theta1 = 0.0

        self.x2 = 0.0
        self.y2 = 0.0
        self.theta2 = 0.0

        self.publisher1 = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )

        self.publisher2 = self.create_publisher(
            Twist,
            "/turtle2/cmd_vel",
            20
        )

        self.timer = self.create_timer(
            0.1,
            self.move_turtle
        )

        self.subscription1 = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.pose_callback1,
            10
        )

        self.subscription2 = self.create_subscription(
            Pose,
            "/turtle2/pose",
            self.pose_callback2,
            10
        )

    def pose_callback1(self, msg):

        self.x1 = msg.x
        self.y1 = msg.y
        self.theta1 = msg.theta

        self.get_logger().info(
            f"X1={self.x1:.2f}, Y1={self.y1:.2f}, Theta1={self.theta1:.2f}"
        )

    def pose_callback2(self, msg):

        self.x2 = msg.x
        self.y2 = msg.y
        self.theta2 = msg.theta

        self.get_logger().info(
            f"X2={self.x2:.2f}, Y2={self.y2:.2f}, Theta2={self.theta2:.2f}"
        )

    def move_turtle(self):

        msg = Twist()

        dx = self.x1 - self.x2
        dy = self.y1 - self.y2

        distance = math.sqrt(dx**2 + dy**2)

        target_angle = math.atan2(dy, dx)

        angle_error = target_angle - self.theta2

        if distance > 0.5:

            msg.linear.x = 2.0
            msg.angular.z = angle_error

        else:

            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.get_logger().info(
            f"Distance={distance:.2f}, Angle Error={angle_error:.2f}"
        )

        self.publisher2.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = MultiRobot_Sub()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
