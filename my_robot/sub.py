#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class MultiRobotPublisher(Node):

    def __init__(self):
        super().__init__("multirobot")

        # Store Turtle1 Pose
        self.x1 = 0.0
        self.y1 = 0.0
        self.theta1 = 0.0

        # Store Turtle2 Pose
        self.x2 = 0.0
        self.y2 = 0.0
        self.theta2 = 0.0

        # Publishers
        self.publisher1 = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )

        self.publisher2 = self.create_publisher(
            Twist,
            "/turtle2/cmd_vel",
            10
        )

        # Subscribers
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

        # Timer
        self.timer = self.create_timer(
            0.1,
            self.move_turtle
        )

    # -----------------------
    # Turtle1 Pose Callback
    # -----------------------
    def pose_callback1(self, msg):

        self.x1 = msg.x
        self.y1 = msg.y
        self.theta1 = msg.theta

    # -----------------------
    # Turtle2 Pose Callback
    # -----------------------
    def pose_callback2(self, msg):

        self.x2 = msg.x
        self.y2 = msg.y
        self.theta2 = msg.theta

    # -----------------------
    # Timer Callback
    # -----------------------
    def move_turtle(self):

        msg1 = Twist()
        msg2 = Twist()

        # Turtle1
        msg1.linear.x = 2.0
        msg1.angular.z = 0.0

        # Turtle2
        msg2.linear.x = 3.0
        msg2.angular.z = 0.0

        self.publisher1.publish(msg1)
        self.publisher2.publish(msg2)

        self.get_logger().info(
            f"T1 -> X={self.x1:.2f}, Y={self.y1:.2f}, Theta={self.theta1:.2f} | "
            f"T2 -> X={self.x2:.2f}, Y={self.y2:.2f}, Theta={self.theta2:.2f}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = MultiRobotPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
