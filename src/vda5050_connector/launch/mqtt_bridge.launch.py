#################
### MQTT Node ###
#################

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
    parameters_config_file = LaunchConfiguration("parameters_config_file")

    # Declare parameters
    robot_namespace = LaunchConfiguration("robot_namespace")
    version_protocol = LaunchConfiguration("version_protocol")
    manufacturer_name = LaunchConfiguration("manufacturer_name")
    serial_number = LaunchConfiguration("serial_number")

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

    # Nodes

    mqtt_bridge_node = Node(
        package="vda5050_connector",
        executable="mqtt_bridge.py",
        namespace=robot_namespace,
        name="mqtt_bridge",
        parameters=[configured_params,
                    {"robot_namespace": robot_namespace},
                    {"manufacturer_name": manufacturer_name},
                    {"serial_number": serial_number},
                    {"version_protocol": version_protocol},
                    ],
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    # Declare parameters
    ld.add_action(declare_parameters_config_file_cmd)

    # Launch nodes
    ld.add_action(mqtt_bridge_node)

    return ld
