#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
import time
class FirstNumber(Node):
    def __init__(self, node_name, *, context = None, cli_args = None, namespace = None, use_global_arguments = True, enable_rosout = True, start_parameter_services = True, parameter_overrides = None, allow_undeclared_parameters = False, automatically_declare_parameters_from_overrides = False, enable_logger_service = False):
        super().__init__(node_name, context=context, cli_args=cli_args, namespace=namespace, use_global_arguments=use_global_arguments, enable_rosout=enable_rosout, start_parameter_services=start_parameter_services, parameter_overrides=parameter_overrides, allow_undeclared_parameters=allow_undeclared_parameters, automatically_declare_parameters_from_overrides=automatically_declare_parameters_from_overrides, enable_logger_service=enable_logger_service)
        self.publisher_ = self.create_publisher(Int64, "number1", 10)
        self.get_logger().info("First number generator has been started now we will send the first number")
         

    def publish_number(self, num):
        msg = Int64()
        msg.data = num
        self.publisher_.publish(msg)
        self.get_logger().info(f"{num} has been published")
        

def main(args=None):
    rclpy.init(args=args)
    node = FirstNumber("adder")
    node.publish_number(3)

if __name__ == "__main__":
    main()
