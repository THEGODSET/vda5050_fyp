####################
### Adapter Node ###
####################

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from vda5050_connector_py.rewritten_yaml import RewrittenYaml
import yaml

def generate_launch_description():
    # Get the launch directory
    adapter_package_name = "vda5050_adapter"
    adapter_package_dir = get_package_share_directory(adapter_package_name)

    # Launch configuration variables for parameters
    robot_namespace = LaunchConfiguration("robot_namespace")
    version_protocol = LaunchConfiguration("version_protocol")
    manufacturer_name = LaunchConfiguration("manufacturer_name")
    serial_number = LaunchConfiguration("serial_number")

    parameters_config_file = os.path.join(adapter_package_dir, "config", "connector.yaml")

    # Create our own temporary YAML files that include substitutions
    configured_params = RewrittenYaml(
        source_file=parameters_config_file,
        root_key=robot_namespace,
        param_rewrites={
            'robot_namespace': robot_namespace,
            'manufacturer_name': manufacturer_name,
            'serial_number': serial_number,
            'version_protocol': version_protocol
        },
        convert_types=True,
    )

    # Adapter node
    agv_adapter_node = Node(
        package=adapter_package_name,
        executable="adapter",
        namespace=robot_namespace,
        name="adapter",
        parameters=[configured_params,
                    {"robot_namespace": robot_namespace},
                    {"manufacturer_name": manufacturer_name},
                    {"serial_number": serial_number},
                    {"version_protocol": version_protocol},
                    ],
    )

    odom_adapter_node = Node(
        package=adapter_package_name,
        executable="odometry",
        # namespace=robot_namespace,
        name='odom_position',
        parameters=[configured_params,
                    {"robot_namespace": robot_namespace},
                    {"manufacturer_name": manufacturer_name},
                    {"serial_number": serial_number},
                    {"version_protocol": version_protocol},
                    ],
    )

    # goal_adapter_node = Node(
    #     package=adapter_package_name,
    #     executable="goal",
    #     # namespace=robot_namespace,
    #     name='goal_adapter',
    #     parameters=[configured_params,
    #                 {"robot_namespace": robot_namespace},
    #                 {"manufacturer_name": manufacturer_name},
    #                 {"serial_number": serial_number},
    #                 {"version_protocol": version_protocol},
    #                 ],
    # )

    # Create the launch description and populate
    ld = LaunchDescription()
    ld.add_action(agv_adapter_node)
    ld.add_action(odom_adapter_node)
    # ld.add_action(goal_adapter_node)

    return ld
