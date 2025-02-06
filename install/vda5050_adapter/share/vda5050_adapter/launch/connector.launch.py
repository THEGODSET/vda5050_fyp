#################
### MAIN FILE ###
#################

# Launches mqtt_bridge, adapter, controller, spawns turtlebot3 in gazebo
# Contains robot specific operation

import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # Get the launch directory
    package_name = "vda5050_adapter"
    package_dir = get_package_share_directory(package_name)

    package_name_connector = "vda5050_connector"
    package_dir_connector = get_package_share_directory(package_name_connector)

    package_name_simulator = "turtlebot3_gazebo"
    package_dir_simulator = get_package_share_directory(package_name_simulator)

    # Launch Configuration
    robot_namespace = LaunchConfiguration("robot_namespace")
    version_protocol = LaunchConfiguration("version_protocol")
    manufacturer_name = LaunchConfiguration("manufacturer_name")
    serial_number = LaunchConfiguration("serial_number")
    x_pose = LaunchConfiguration("x_pose")
    y_pose = LaunchConfiguration("y_pose")

    parameters_config_file = LaunchConfiguration("parameters_config_file")
    declare_parameters_config_file_cmd = DeclareLaunchArgument(
        "parameters_config_file",
        default_value=os.path.join(package_dir, "config", "connector.yaml"),
        description="Full path to the parameters config file to use",
    )

    # Nodes
    mqtt_bridge_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_dir_connector, "launch", "mqtt_bridge.launch.py")
        ),
        launch_arguments={
            "robot_namespace": robot_namespace,
            "version_protocol": version_protocol,
            "manufacturer_name": manufacturer_name,
            "serial_number": serial_number,
            "parameters_config_file": parameters_config_file,
        }.items(),
    )

    controller_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_dir_connector, "launch", "controller.launch.py")
        ),
        launch_arguments={
            "robot_namespace": robot_namespace,
            "version_protocol": version_protocol,
            "manufacturer_name": manufacturer_name,
            "serial_number": serial_number,
            "parameters_config_file": parameters_config_file,
        }.items(),
    )

    spawn_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_dir_simulator, "launch", "spawn_multiple_entity_with_nav.launch.py")
            ),
            launch_arguments={
                "namespace": robot_namespace,
                "x_pose": x_pose,
                "y_pose": y_pose,
                "use_sim_time": "true",
                "enable_drive": "false",
                "enable_rviz": "true",
                "rviz_config_file": os.path.join(package_dir_simulator, "rviz", "multi_nav2_default_view.rviz"),
                "nav_params_file": os.path.join(package_dir_simulator, "params", "nav2_params.yaml"),
            }.items()
    )

    adapter_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_dir, "launch", "adapter.launch.py")
        ),
        launch_arguments={
            "robot_namespace": robot_namespace,
            "version_protocol": version_protocol,
            "manufacturer_name": manufacturer_name,
            "serial_number": serial_number,
            "parameters_config_file": parameters_config_file,
        }.items(),
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    # ld.add_action(declare_namespace)
    ld.add_action(declare_parameters_config_file_cmd)

    # Launch nodes
    ld.add_action(spawn_node)
    ld.add_action(mqtt_bridge_node)
    ld.add_action(controller_node)
    ld.add_action(adapter_node)

    return ld

"""
This launch file launches the following nodes:
- mqtt_bridge_node - MQTT bridge
- controller_node - Controller
- spawn_node - Spawns turtlebot3
- adapter_node - Adapter for turtlebot3
"""