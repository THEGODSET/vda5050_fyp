#!/usr/bin/env python3
import os
import yaml

# Import necessary ROS 2 dependencies
import rclpy
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node

from datetime import datetime, timezone

from vda5050_msgs.msg import Header

# Import custom utility functions and message types
from vda5050_connector_py.utils import read_parameter

# VDA5050 messages
from ament_index_python.packages import get_package_share_directory

from vda5050_adapter import position_adapter
from vda5050_connector_py import mqtt_bridge

NODE_NAME = "agv_adapter"

class on_field_agv(Node):
    def __init__(self):
        super().__init__(NODE_NAME)
        self.logger = self.get_logger()

        self.agv_detail()

        self.vda5050_header_msg(1)
        # self.position = position_adapter()

        self.logger.info("Node {} has started successfully.".format(NODE_NAME))

    def agv_detail(self):
        self._robot_namespace = read_parameter(self, 'robot_namespace', 'robot_namespace', str)
        self._manufacturer_name = read_parameter(self, 'manufacturer_name', 'manufacturer_name', str)
        self._serial_number = read_parameter(self, 'serial_number', 'serial_number', str)
        self._version_protocol = read_parameter(self, 'version_protocol', 'version_protocol', str)

        self._robot_namespace = self.get_parameter('robot_namespace').value
        self._version_protocol = self.get_parameter('version_protocol').value
        self._manufacturer_name = self.get_parameter('manufacturer_name').value
        self._serial_number = self.get_parameter('serial_number').get_parameter_value().string_value

    def vda5050_header_msg(self, num_header=1):
        header = Header()
        header.manufacturer = self._manufacturer_name
        header.serial_number = self._serial_number
        header.version = self._version_protocol
        header.timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.') + f'{datetime.now(timezone.utc).microsecond // 1000:03d}Z'
        if num_header == 1:
            header.header_id = num_header
            num_header+=1
        else:
            num_header+=1
            header.header_id = num_header
        self.logger.info(str(header))
        return header
    
    # def order_message(self):
    #     mqtt_bridge


def main(args=None):
    rclpy.init(args=args)
    agv_adapter = on_field_agv()

    executor = MultiThreadedExecutor()

    executor.add_node(agv_adapter)

    executor.spin()

    # rclpy.spin(agv_adapter)
    agv_adapter.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()