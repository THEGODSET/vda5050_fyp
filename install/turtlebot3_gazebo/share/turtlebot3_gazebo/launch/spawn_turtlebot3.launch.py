import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Ensure TURTLEBOT3_MODEL is set
    TURTLEBOT3_MODEL = os.environ.get('TURTLEBOT3_MODEL')
    if not TURTLEBOT3_MODEL:
        raise EnvironmentError(
            "The environment variable TURTLEBOT3_MODEL is not set. Please set it to 'burger', 'waffle', or 'waffle_pi'."
        )

    # Define URDF file path
    model_folder = f'turtlebot3_{TURTLEBOT3_MODEL}'
    urdf_path = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'models', model_folder, 'model.sdf'
    )
    assert os.path.exists(urdf_path), f"URDF file not found: {urdf_path}"

    # Launch configuration variables
    x_pose = LaunchConfiguration('x_pose', default='0.0')
    y_pose = LaunchConfiguration('y_pose', default='0.0')
    namespace = LaunchConfiguration('namespace', default='robot1')

    # Declare the launch arguments
    declare_x_position_cmd = DeclareLaunchArgument(
        'x_pose', default_value='0.0', description='Initial X position of the robot')
    declare_y_position_cmd = DeclareLaunchArgument(
        'y_pose', default_value='0.0', description='Initial Y position of the robot')
    declare_namespace_cmd = DeclareLaunchArgument(
        'namespace', default_value='robot1', description='Namespace of the robot')


    # Node to spawn the robot in Gazebo
    start_gazebo_ros_spawner_cmd = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        namespace=namespace,
        arguments=[
            '-entity', namespace,
            '-file', urdf_path,
            '-robot_namespace', namespace,
            '-x', x_pose,
            '-y', y_pose,
            '-z', '0.01'
        ],
        output='screen',
    )

    # Create launch description and add actions
    ld = LaunchDescription()

    ld.add_action(declare_x_position_cmd)
    ld.add_action(declare_y_position_cmd)
    ld.add_action(declare_namespace_cmd)
    ld.add_action(start_gazebo_ros_spawner_cmd)

    return ld
