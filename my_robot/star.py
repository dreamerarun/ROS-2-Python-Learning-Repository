#!/usr/bin/env python3

import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class StarDrawer(Node):

    def __init__(self):
        super().__init__("star_drawer")

        # Current pose
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # Starting pose
        self.start_x = 0.0
        self.start_y = 0.0
        self.start_theta = 0.0

        # Wait until first pose is received
        self.pose_received = False

        # Shape parameters
        self.line_length = 2.0
        self.turn_angle = math.radians(144)   # 144 degrees
        self.total_lines = 5

        # FSM variables
        self.state = "MOVE"
        self.line = 0

        # Publisher
        self.publisher = self.create_publisher(
            Twist,
            "/turtle1/cmd_vel",
            10
        )

        # Subscriber
        self.subscription = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.pose_callback,
            10
        )

        # Timer (50 Hz)
        self.timer = self.create_timer(
            0.02,
            self.control_loop
        )

    def pose_callback(self, msg):

        self.x = msg.x
        self.y = msg.y
        self.theta = msg.theta

        if not self.pose_received:
            self.start_x = self.x
            self.start_y = self.y
            self.start_theta = self.theta
            self.pose_received = True

    def control_loop(self):

        if not self.pose_received:
            return

        msg = Twist()

        # Finished drawing
        if self.line >= self.total_lines:

            msg.linear.x = 0.0
            msg.angular.z = 0.0

            self.publisher.publish(msg)

            self.get_logger().info("⭐ Star Completed!")

            return

        # =====================
        # MOVE STATE
        # =====================

        if self.state == "MOVE":

            distance = math.sqrt(
                (self.x - self.start_x) ** 2 +
                (self.y - self.start_y) ** 2
            )

            if distance < self.line_length:

                msg.linear.x = 2.0
                msg.angular.z = 0.0

            else:

                msg.linear.x = 0.0
                msg.angular.z = 0.0

                self.start_theta = self.theta
                self.state = "TURN"

                self.get_logger().info(
                    f"Finished Line {self.line + 1}"
                )

        # =====================
        # TURN STATE
        # =====================

        elif self.state == "TURN":

            angle = abs(
                math.atan2(
                    math.sin(self.theta - self.start_theta),
                    math.cos(self.theta - self.start_theta)
                )
            )

            if angle < self.turn_angle:

                msg.linear.x = 0.0
                msg.angular.z = 0.8

            else:

                msg.linear.x = 0.0
                msg.angular.z = 0.0

                self.line += 1

                self.start_x = self.x
                self.start_y = self.y
                self.start_theta = self.theta

                self.state = "MOVE"

                self.get_logger().info(
                    f"Completed {self.line}/{self.total_lines}"
                )

        self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = StarDrawer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
