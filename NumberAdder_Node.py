#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class Adder_Here(Node):
    def __init__(self, node_name, *, context = None, cli_args = None, namespace = None, use_global_arguments = True, enable_rosout = True, start_parameter_services = True, parameter_overrides = None, allow_undeclared_parameters = False, automatically_declare_parameters_from_overrides = False, enable_logger_service = False):
        super().__init__(node_name, context=context, cli_args=cli_args, namespace=namespace, use_global_arguments=use_global_arguments, enable_rosout=enable_rosout, start_parameter_services=start_parameter_services, parameter_overrides=parameter_overrides, allow_undeclared_parameters=allow_undeclared_parameters, automatically_declare_parameters_from_overrides=automatically_declare_parameters_from_overrides, enable_logger_service=enable_logger_service)

        self.subscriber_ = self.create_subscription(Int64, "number1", self.msg1_callback,10)
        self.subscriber2_ = self.create_subscription(Int64, "number2", self.msg2_callback, 10)
        self.sum1 = 0
        self.num1 = None
        self.num2 = None
    def msg1_callback(self, msg: Int64):
        self.num1 = msg.data
         
    def msg2_callback(self, msg: Int64):
        self.num2 = msg.data
        self.try_add(self.num1, self.num2)

    def try_add(self,num1, num2):
        self.sum1 = num1+num2
        self.get_logger().info(f"Sum = {self.num1} + {self.num2} = {self.sum1}")
 

def main(args=None):
    rclpy.init(args=args)
    node = Adder_Here("SubscriberNode")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
