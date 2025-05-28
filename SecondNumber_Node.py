#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
import time 
class SecondNumber(Node):
    def __init__(self):
        super().__init__('second_number')
        self.publisher_ = self.create_publisher(Int64, "number2", 10)
        self.get_logger().info("The second number publisher has been started")

    def publish_number(self, num):
        msg = Int64()
        msg.data = num
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")

def main():
    rclpy.init()
    node = SecondNumber()
    node.publish_number(3)
         
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":  
    main()
