import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch import LaunchDescription
from launch_ros.actions import Node, PushRosNamespace
from launch.substitutions import LaunchConfiguration
from vda5050_connector_py.rewritten_yaml import RewrittenYaml


def generate_launch_description():
    robot_namespace = 'turtlebot0'

    PushRosNamespace(robot_namespace)

    # Get the launch directory
    adapter_package_name = "vda5050_adapter"
    adapter_package_dir = get_package_share_directory(adapter_package_name)

    # Launch configuration variables for parameters
    namespace = LaunchConfiguration("namespace")
    parameters_config_file = LaunchConfiguration("parameters_config_file")

    declare_namespace = DeclareLaunchArgument(
        "namespace",
        default_value="vda5050_connector",
        description="Namespace to use",
    )

    declare_parameters_config_file_cmd = DeclareLaunchArgument(
        "parameters_config_file",
        default_value=os.path.join(adapter_package_dir, "config", "connector.yaml"),
        description="Full path to the parameters config file to use",
    )

    # Create our own temporary YAML files that include substitutions
    configured_params = RewrittenYaml(
        source_file=parameters_config_file,
        root_key=namespace,
        param_rewrites={},
        convert_types=False,
    )

    # Adapter node
    adapter_node = Node(
        package=adapter_package_name,
        executable="adapter",
        namespace=namespace,
        name="adapter",
        parameters=[configured_params],
        remappings=[
            ('/cmd_vel', f'/{robot_namespace}/cmd_vel'),  # Remap cmd_vel to robot's cmd_vel
            ('/status', f'/{robot_namespace}/status'),  # Remap status to robot's status
            ('/vda5050/state', f'/{robot_namespace}/vda5050/state'),  # Remap state topic
            ('/vda5050/commands', f'/{robot_namespace}/vda5050/commands'),  # Remap commands topic
        ]
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(declare_namespace)
    ld.add_action(declare_parameters_config_file_cmd)
    ld.add_action(adapter_node)

    return ld
