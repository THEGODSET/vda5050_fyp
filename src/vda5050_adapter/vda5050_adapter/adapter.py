#!/usr/bin/env python3

# BSD 3-Clause License
#
# Copyright 2022 InOrbit, Inc.
# Copyright 2022 Clearpath Robotics, Inc.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the InOrbit, Inc. nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Import necessary ROS 2 dependencies
import rclpy
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action import ActionClient
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

import tf_transformations
import time

# Import custom utility functions and message types
from vda5050_connector_py.utils import read_str_parameter
from vda5050_connector.action import NavigateToNode
from vda5050_connector.action import ProcessVDAAction
from nav2_msgs.action import NavigateToPose
from vda5050_connector.srv import GetState
from vda5050_connector.srv import SupportedActions
from nav_msgs.msg import Odometry

# TF2 for transforming frames
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

# Import geometry-related messages
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
from vda5050_msgs.msg import Node as VDANode
from vda5050_msgs.msg import AGVPosition as VDAAGVPosition
from vda5050_msgs.msg import Velocity as VDAVelocity
from vda5050_msgs.msg import OrderState as VDAOrderState
from vda5050_msgs.msg import CurrentAction as VDACurrentAction

# Define the name of the node
NODE_NAME = "tb3_adapter"

# Define the TB3Adapter class, which inherits from Node
class TB3Adapter(Node):
    def __init__(self):
        # Initialize the node with the name 'tb3_adapter'
        super().__init__(NODE_NAME)
        self.logger = self.get_logger()

        # Initialize AGV position, velocity, and driving status
        self._agv_position = VDAAGVPosition()
        self._velocity = VDAVelocity()
        self._driving = False

        # Placeholder for the active node to be navigated to
        self._active_node = VDANode()

        # Call configuration method to set up parameters and services
        self.on_configure()
        self.logger.info("Node {} has started successfully.".format(NODE_NAME))

    def on_configure(self):
        # Read parameters for robot name, manufacturer, and services
        self.read_parameters()

        # Set up the base interface name using the robot's namespace and name
        base_interface_name = (
            f"{self.get_namespace()}/{self._manufacturer_name}/{self._robot_name}/"
        )

        # Create services for retrieving state and supported actions
        self.get_adapter_state_srv = self.create_service(
            srv_type=GetState,
            srv_name=base_interface_name + self._get_state_svc_srv,
            callback=self.get_state_callback,
        )

        self.supported_actions_srv = self.create_service(
            SupportedActions,
            base_interface_name + self._supported_actions_svc_srv,
            lambda _: self.get_logger().info("Supported actions request"),
        )

        # Create action server for navigating to nodes
        nav_to_node_action_client_cb_group = MutuallyExclusiveCallbackGroup()
        self._nav_to_node_ac_srv = ActionServer(
            node=self,
            action_type=NavigateToNode,
            action_name=base_interface_name + self._nav_to_node_act_srv,
            execute_callback=self.navigate_to_node_callback,
            callback_group=nav_to_node_action_client_cb_group,
        )

        # Create action server for processing VDA actions
        self._process_vda_action_ac_srv = ActionServer(
            node=self,
            action_type=ProcessVDAAction,
            action_name=base_interface_name + self._vda_action_act_srv,
            execute_callback=self.process_vda_action_callback,
        )

        # Create an action client for navigation to a pose using TurtleBot 3
        nav_to_pose_tb3_action_client_cb_group = MutuallyExclusiveCallbackGroup()
        self._nav_to_pose_tb3_action_client = ActionClient(
            node=self,
            action_type=NavigateToPose,
            action_name="/navigate_to_pose",
            callback_group=nav_to_pose_tb3_action_client_cb_group,
        )

        # Create a publisher for the initial pose to be sent to the robot
        self._init_pose_pub = self.create_publisher(
            PoseWithCovarianceStamped, "/initialpose", 10
        )

        # Set up the TF buffer and listener for transforming coordinates
        self._tf_buffer = Buffer()
        self._tf_listener = TransformListener(self._tf_buffer, self)

        # Subscribe to the robot's odometry to get its position and velocity
        self._odom_sub = self.create_subscription(
            Odometry, "/odom", self.odom_callback, 10
        )

    def read_parameters(self):
        # Read robot parameters like its name, manufacturer, and serial number
        self._robot_name = read_str_parameter(self, "robot_name", "robot_1")
        self._manufacturer_name = read_str_parameter(self, "manufacturer_name", "robots")
        self._serial_number = read_str_parameter(self, "serial_number", "robot_1")

        # Read service names for getting state, VDA actions, etc.
        self._get_state_svc_srv = read_str_parameter(self, "get_state_svc_name", "adapter/get_state")
        self._vda_action_act_srv = read_str_parameter(self, "vda_action_act_name", "adapter/vda_action")
        self._nav_to_node_act_srv = read_str_parameter(self, "nav_to_node_act_name", "adapter/nav_to_node")
        self._supported_actions_svc_srv = read_str_parameter(self, "supported_actions_svc_name", "adapter/supported_actions")

    def odom_callback(self, odom_msg: Odometry):
        # Handle incoming odometry messages to track robot's position and velocity
        to_frame = "map"
        from_frame = "base_link"
        self._agv_position.map_id = to_frame

        try:
            # Get the transformation from 'base_link' to 'map' frame
            now = rclpy.time.Time()
            trans = self._tf_buffer.lookup_transform(to_frame, from_frame, now)

            # Update AGV position (x, y, theta) based on the transform
            self._agv_position.x = trans.transform.translation.x
            self._agv_position.y = trans.transform.translation.y

            # Convert quaternion rotation to Euler angles to get theta
            q = trans.transform.rotation
            _, _, theta = tf_transformations.euler_from_quaternion((q.x, q.y, q.z, q.w))
            self._agv_position.theta = theta
        except TransformException as ex:
            # Log if the transformation failed
            self.get_logger().info(
                "Could not transform {} to {}: {}".format(to_frame, from_frame, ex)
            )
            return

        # Update the robot's velocity from the odometry message
        self._velocity.vx = odom_msg.twist.twist.linear.x
        self._velocity.vy = odom_msg.twist.twist.linear.y
        self._velocity.omega = odom_msg.twist.twist.angular.z

    def get_state_callback(self, request, response):
        # Respond to requests for the current state of the AGV (position, velocity)
        order_state = VDAOrderState()
        order_state.agv_position = self._agv_position
        order_state.velocity = self._velocity
        response.state = order_state
        return response

    def process_vda_action_callback(self, goal_handle):
        # Handle incoming VDA action requests (e.g., robot initialization or custom actions)
        action = goal_handle.request.action
        result = ProcessVDAAction.Result()

        # Parse action parameters into a dictionary
        action_parameters = {}
        for action_parameter in action.action_parameters:
            action_parameters[action_parameter.key] = action_parameter.value

        self.logger.info(f"Parsed action parameters: {action_parameters}")

        if action.action_type == "initPosition":
            # Initialize robot position based on action parameters
            init_pose = PoseWithCovarianceStamped()
            init_pose.header.stamp = self.get_clock().now().to_msg()
            init_pose.header.frame_id = "map"
            init_pose.pose.pose.position.x = float(action_parameters["x"])
            init_pose.pose.pose.position.y = float(action_parameters["y"])
            init_pose.pose.pose.position.z = 0.0

            # Send the initial pose to the robot
            self._init_pose_pub.publish(init_pose)
            self.logger.info(f"Initial position set: {action_parameters['x']}, {action_parameters['y']}")

        return result

    def navigate_to_node_callback(self, goal_handle):
        # Callback to execute navigation to a node in the VDA adapter protocol
        goal = goal_handle.request
        nav_pose = PoseStamped()
        nav_pose.header.frame_id = "map"
        nav_pose.pose.position.x = goal.target_node.x
        nav_pose.pose.position.y = goal.target_node.y
        nav_pose.pose.orientation.w = 1.0  # Placeholder for orientation

        self._nav_to_pose_tb3_action_client.send_goal_async(nav_pose)
        return NavigateToNode.Result()

def main(args=None):
    rclpy.init(args=args)
    node = TB3Adapter()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
