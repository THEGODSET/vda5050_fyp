import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    package_name = "vda5050_adapter"
    package_dir = get_package_share_directory(package_name)

    package_name_connector = "vda5050_connector"
    package_dir_connector = get_package_share_directory(package_name_connector)

    namespace = LaunchConfiguration("namespace")
    parameters_config_file = LaunchConfiguration("parameters_config_file")

    declare_namespace = DeclareLaunchArgument(
        "namespace",
        default_value="vda5050_connector",
        description="Namespace to use",
    )

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
            "namespace": namespace,
            "parameters_config_file": parameters_config_file,
        }.items(),
    )

    controller_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_dir_connector, "launch", "controller.launch.py")
        ),
        launch_arguments={
            "namespace": namespace,
            "parameters_config_file": parameters_config_file,
        }.items(),
    )

    adapter_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(package_dir, "launch", "adapter_tb3.launch.py")
        ),
        launch_arguments={
            "namespace": namespace,
            "parameters_config_file": parameters_config_file,
        }.items(),
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(declare_namespace)
    ld.add_action(declare_parameters_config_file_cmd)

    # Launch nodes
    ld.add_action(mqtt_bridge_node)
    ld.add_action(controller_node)
    ld.add_action(adapter_node)

    return ld
