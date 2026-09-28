#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from turtlesim.srv import Spawn


class SpawnClient(Node):

    def __init__(self):

        # Create the node
        super().__init__("spawn_client")

        # Create a client for the /spawn service
        self.client = self.create_client(
            Spawn,
            "/spawn"
        )

        # Wait until the service becomes available
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for /spawn service...")

        # Create a request object
        self.request = Spawn.Request()

        # Fill the request
        self.request.x = 3.0
        self.request.y = 5.0
        self.request.theta = 0.0
        self.request.name = "turtle2"

        # Send the request
        self.future = self.client.call_async(self.request)

        # Execute this function when the response arrives
        self.future.add_done_callback(self.response_callback)

    def response_callback(self, future):

        response = future.result()

        self.get_logger().info(
            f"Turtle Spawned Successfully : {response.name}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = SpawnClient()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
