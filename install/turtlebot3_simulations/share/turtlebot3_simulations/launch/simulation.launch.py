#################
### MAIN FILE ###
#################

# Launches mqtt_bridge, adapter, controller

import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import PushRosNamespace
import yaml


def generate_launch_description():

    package_name = "vda5050_adapter"
    package_dir = get_package_share_directory(package_name)

    package_name_simulator = "turtlebot3_gazebo"
    package_dir_simulator = get_package_share_directory(package_name_simulator)

    # Nodes

    simulation_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_dir_simulator, "launch", "turtlebot3_maze.launch.py")
            ),
            launch_arguments={
                "use_sim_time": "true",
            }.items()
    )

    connector_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_dir, "launch", "connector.launch.py")
        ),
        launch_arguments={
            "robot_namespace": "turtlebot0",
            "version_protocol": "2.0.0",
            "manufacturer_name": "Robotis",
            "serial_number": "s028784",
            "x_pose": "-1.0",
            "y_pose": "-0.5"
        }.items(),
    )

    # second_connector_node = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join(package_dir, "launch", "connector.launch.py")
    #     ),
    #     launch_arguments={
    #         "robot_namespace": "turtlebot1",
    #         "version_protocol": "2.0.0",
    #         "manufacturer_name": "Kuka",
    #         "serial_number": "s458762",
    #         "x_pose": "-2.0",
    #         "y_pose": "0.0"
    #     }.items(),
    # )

    # Create the launch description and populate
    ld = LaunchDescription()

    # Launch nodes
    ld.add_action(simulation_node)
    ld.add_action(connector_node)
    # ld.add_action(second_connector_node)

    return ld
