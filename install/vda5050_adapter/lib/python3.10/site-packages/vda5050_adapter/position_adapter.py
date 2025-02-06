#!/usr/bin/env python3

# Import necessary ROS 2 dependencies
import rclpy
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action import ActionClient
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

import time

# Import custom utility functions and message types
from vda5050_connector_py.utils import read_parameter
from vda5050_connector.action import NavigateToNode
from vda5050_connector.action import ProcessVDAAction
from nav2_msgs.action import NavigateToPose
from vda5050_connector.srv import GetState
from vda5050_connector.srv import SupportedActions
from nav_msgs.msg import Odometry

import tf_transformations

# TF2 for transforming frames
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

# Import geometry-related messages
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped

# VDA5050 messages
from vda5050_msgs.msg import Node as VDANode
from vda5050_msgs.msg import AGVPosition as VDAAGVPosition
from vda5050_msgs.msg import Velocity as VDAVelocity
from vda5050_msgs.msg import OrderState as VDAOrderState
from vda5050_msgs.msg import CurrentAction as VDACurrentAction

from vda5050_connector_py import vda5050_controller

NODE_NAME = "position_adapter"

class odometry_status(Node):
    def __init__(self):
        super().__init__(NODE_NAME)
        
        # Parameters
        self.launch_parameters()

        # Initialize the AGV position message
        self.odom_position = VDAAGVPosition()
        self.velocity = VDAVelocity()
        self.driving = False

        # self.position_node = VDANode()

        
        self.on_configure()

        # Store map_id (fixed to 'map' for simplicity)
        self.odom_position.map_id = "map"

    def launch_parameters(self):
        self.robot_namespace = self.get_parameter("robot_namespace").get_parameter_value().string_value
        self.manufacturer_name = self.get_parameter("manufacturer_name").get_parameter_value().string_value
        self.serial_number = self.get_parameter("serial_number").get_parameter_value().string_value
        self.version_protocol = self.get_parameter("version_protocol").get_parameter_value().string_value

    def on_configure(self):
        base_interface_name = (
            f"{self.version_protocol}/{self.manufacturer_name}/{self.serial_number}/"
        )

        self.get_adapter_state_srv = self.create_service(
            srv_type=GetState,
            srv_name=base_interface_name + vda5050_controller.DEFAULT_GET_STATE_SVC_NAME,
            callback=self.get_state_callback,
        )

        self.supported_actions_srv = self.create_service(
            SupportedActions,
            base_interface_name + vda5050_controller.DEFAULT_SUPPORTED_ACTIONS_SVC_NAME,
            lambda _: self.get_logger().info("Supported actions request"),
        )

        nav_to_node_action_client_cb_group = MutuallyExclusiveCallbackGroup()
        self.nav_to_node_ac_srv = ActionServer(
            node=self,
            action_type=NavigateToNode,
            action_name=base_interface_name + vda5050_controller.DEFAULT_NAV_TO_NODE_ACT_NAME,
            execute_callback=self.navigate_to_node_callback,
            callback_group=nav_to_node_action_client_cb_group,
        )

        self.process_vda_action_ac_srv = ActionServer(
            node=self,
            action_type=ProcessVDAAction,
            action_name=base_interface_name + vda5050_controller.DEFAULT_VDA_ACTION_ACT_NAME,
            execute_callback=self.process_vda_action_callback,
        )

        nav_to_pose_tb3_action_client_cb_group = MutuallyExclusiveCallbackGroup()
        self.nav_to_pose_tb3_action_client = ActionClient(
            node=self,
            action_type=NavigateToPose,
            action_name=f"{self.robot_namespace}/navigate_to_pose",
            callback_group=nav_to_pose_tb3_action_client_cb_group,
        )

        self.init_pose_pub = self.create_publisher(
            PoseWithCovarianceStamped, f"{self.robot_namespace}/initialpose", 10
        )

        # TF
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.odom_sub = self.create_subscription(
            Odometry, f"{self.robot_namespace}/odom", self.odom_callback, 10
        )

    def position(self, odom_msg: Odometry):
        to_frame = "map"
        from_frame = "base_link"
        self.odom_position.map_id = to_frame

        try:
            now = rclpy.time.Time()
            trans = self.tf_buffer.lookup_transform(to_frame, from_frame, now)

            self.odom_position.x = trans.transform.translation.x
            self.odom_position.y = trans.transform.translation.y

            q = trans.transform.rotation
            _, _, theta = tf_transformations.euler_from_quaternion((q.x, q.y, q.z, q.w))
            self.odom_position.theta = theta
        except TransformException as ex:
            self.get_logger().info(
                "Could not transform {} to {}: {}".format(to_frame, from_frame, ex)
            )
            return

        # Twist
        self.velocity.vx = odom_msg.twist.twist.linear.x
        self.velocity.vy = odom_msg.twist.twist.linear.y
        self.velocity.omega = odom_msg.twist.twist.angular.z

    def get_state_callback(self, request, response):
        order_state = VDAOrderState()
        order_state.agv_position = self.agv_position
        order_state.velocity = self.velocity
        response.state = order_state
        return response

    def process_vda_action_callback(self, goal_handle):
        action = goal_handle.request.action
        result = ProcessVDAAction.Result()

        action_parameters = {}
        for action_parameter in action.action_parameters:
            action_parameters[action_parameter.key] = action_parameter.value

        self.logger.info(f"Parsed action parameters: {action_parameters}")

        if action.action_type == "initPosition":
            pose_with_cov_stamped = PoseWithCovarianceStamped()
            pose_with_cov_stamped.header.frame_id = action_parameters["mapId"]

            pose_with_cov_stamped.pose.pose.position.x = float(action_parameters["x"])
            pose_with_cov_stamped.pose.pose.position.y = float(action_parameters["y"])

            q = tf_transformations.quaternion_from_euler(
                0, 0, float(action_parameters["theta"])
            )
            pose_with_cov_stamped.pose.pose.orientation.x = q[0]
            pose_with_cov_stamped.pose.pose.orientation.y = q[1]
            pose_with_cov_stamped.pose.pose.orientation.z = q[2]
            pose_with_cov_stamped.pose.pose.orientation.w = q[3]

            self._init_pose_pub.publish(pose_with_cov_stamped)

            self.logger.info(f"Instant action '{action.action_id}' finished")

            result.result = VDACurrentAction(
                action_id=action.action_id,
                action_description=action.action_description,
                action_status=VDACurrentAction.FINISHED,
            )

        else:
            self.logger.info(
                f"Received unsupported action: '{action.action_type}'. "
                "Beep Boop Bop ... doing robot stuff"
            )

            current_action = VDACurrentAction(
                action_id=action.action_id,
                action_description=action.action_description,
                action_status=VDACurrentAction.INITIALIZING,
            )
            feedback_msg = ProcessVDAAction.Feedback(current_action=current_action)

            # Publish feedback with different actions states back to the
            # controller while waiting 5 seconds between feedback messages
            for action_status in [
                VDACurrentAction.INITIALIZING,
                VDACurrentAction.RUNNING,
                VDACurrentAction.PAUSED,
                VDACurrentAction.RUNNING,
                VDACurrentAction.FINISHED,
            ]:
                feedback_msg.current_action.action_status = action_status
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(3)

            result.result = feedback_msg.current_action
        goal_handle.succeed()

        return result

    def navigate_to_node_callback(self, goal_handle):
        node = goal_handle.request.node

        self.logger.info(
            f"Navigating to node '{goal_handle.request.node}', edge '{goal_handle.request.edge}'"
        )

        self._active_node = node
        goal_point = PoseStamped()

        goal_point.header.stamp = self.get_clock().now().to_msg()
        goal_point.header.frame_id = node.node_position.map_id

        goal_point.pose.position.x = node.node_position.x
        goal_point.pose.position.y = node.node_position.y

        q = tf_transformations.quaternion_from_euler(0, 0, node.node_position.theta)
        goal_point.pose.orientation.x = q[0]
        goal_point.pose.orientation.y = q[1]
        goal_point.pose.orientation.z = q[2]
        goal_point.pose.orientation.w = q[3]

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = goal_point

        self._nav_to_pose_tb3_action_client.wait_for_server()

        self.get_logger().info("Async goal for robot {} sent.".format("turtlebot_3"))

        self._nav_to_pose_tb3_send_goal_future = (
            self._nav_to_pose_tb3_action_client.send_goal_async(goal_msg)
        )
        self._driving = True

        self._nav_to_pose_tb3_send_goal_future.add_done_callback(
            self._nav_to_pose_tb3_goal_response_callback
        )

        while self._driving:
            pass

        goal_handle.succeed()

        result = NavigateToNode.Result()
        return result

    # Callbacks

    def nav_to_pose_tb3_goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected :(")
            return

        self.get_logger().info("Goal accepted :)")
        goal_handle.get_result_async().add_done_callback(
            self._nav_to_pose_tb3_get_result_callback
        )

    def nav_to_pose_tb3_get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info("Result: {}".format(result))
        self._driving = False
        self.get_logger().info(
            "The actions to do are: {}".format(self._active_node.actions)
        )

    def odom_callback(self, odom_msg: Odometry):
        # Define the frames to transform between
        to_frame = "map"
        from_frame = "base_link"
        
        try:
            # Get the current transformation from base_link to map
            now = self.get_clock().now()
            trans = self._tf_buffer.lookup_transform(to_frame, from_frame, now)
            
            # Extract position from the transformation and set it in AGVPosition message
            self._agv_position.x = trans.transform.translation.x
            self._agv_position.y = trans.transform.translation.y
            
            # Extract orientation and convert to Euler angles
            q = trans.transform.rotation
            _, _, theta = tf_transformations.euler_from_quaternion((q.x, q.y, q.z, q.w))
            self._agv_position.theta = theta
            
            # Log the AGV position
            self.get_logger().info(f"AGV Position: x={self._agv_position.x}, y={self._agv_position.y}, theta={self._agv_position.theta}")
        
        except TransformException as ex:
            self.get_logger().warn(f"Could not transform {to_frame} to {from_frame}: {ex}")
            return

def main(args=None):
    rclpy.init(args=args)
    odom_adapter_node = odometry_status()

    executor = MultiThreadedExecutor()
    executor.add_node(odom_adapter_node)

    executor.spin()

    odom_adapter_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()