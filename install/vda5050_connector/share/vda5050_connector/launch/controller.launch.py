#######################
### Controller Node ###
#######################

# Import dependencies
import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from vda5050_connector_py.rewritten_yaml import RewrittenYaml


def generate_launch_description():

    # Get the launch directory
    package_name = "vda5050_connector"
    package_dir = get_package_share_directory(package_name)

    # Launch configuration variables for parameters
    robot_namespace = LaunchConfiguration("robot_namespace")
    parameters_config_file = LaunchConfiguration("parameters_config_file")
    version_protocol = LaunchConfiguration("version_protocol")
    manufacturer_name = LaunchConfiguration("manufacturer_name")
    serial_number = LaunchConfiguration("serial_number")
    

    declare_namespace = DeclareLaunchArgument(
        "robot_namespace",
        default_value="vda5050",
        description="Namespace to use",
    )

    declare_parameters_config_file_cmd = DeclareLaunchArgument(
        "parameters_config_file",
        default_value=os.path.join(package_dir, "config", "connector_example.yaml"),
        description="Full path to the parameters config file to use",
    )

    # Create our own temporary YAML files that include substitutions
    configured_params = RewrittenYaml(
        source_file=parameters_config_file,
        root_key=robot_namespace,
        param_rewrites={},
        convert_types=False,
    )

    # Adapter node
    controller_node = Node(
        package=package_name,
        executable="vda5050_controller.py",
        namespace=robot_namespace,
        name="controller",
        parameters=[configured_params,
                    {"robot_namespace": robot_namespace},
                    {"manufacturer_name": manufacturer_name},
                    {"serial_number": serial_number},
                    {"version_protocol": version_protocol},
                    ],
        arguments=[],
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(declare_namespace)
    ld.add_action(declare_parameters_config_file_cmd)

    ld.add_action(controller_node)

    return ld
