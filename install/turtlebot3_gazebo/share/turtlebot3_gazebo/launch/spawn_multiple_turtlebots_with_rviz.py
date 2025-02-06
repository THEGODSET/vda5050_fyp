import os
from time import sleep
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    # Set the number of robots and the map environment
    num_robots = 3  # Number of TurtleBots you want to spawn
    base_namespace = 'robot'  # Base namespace for the robots
    robot_model = 'burger'  # Model type, e.g., burger, waffle
    map_file = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'map', 'map_maze.yaml')  # Your map file

    # Initialize the launch configurations
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # Get the paths for the URDF and SDF models for the TurtleBot
    TURTLEBOT3_MODEL = os.getenv('TURTLEBOT3_MODEL', robot_model)
    model_folder = 'turtlebot3_' + TURTLEBOT3_MODEL
    sdf_path = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'models',
        model_folder,
        'model.sdf'
    )
    urdf_file_name = 'turtlebot3_' + TURTLEBOT3_MODEL + '.urdf'
    urdf_path = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'urdf',
        urdf_file_name
    )
    assert os.path.exists(urdf_path), "TurtleBot URDF doesn't exist at " + str(urdf_path)

    # Spawn robots in unique positions
    spawn_commands = []
    rviz_commands = []
    for i in range(num_robots):
        namespace = f'{base_namespace}{i+1}'
        x_pose = 2 * (i + 1)  # Incremental X position for each robot
        y_pose = 2 * (i + 1)  # Incremental Y position for each robot
        spawn_cmd = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            namespace=namespace,
            arguments=[
                '-entity', namespace,
                '-file', sdf_path,
                '-x', str(x_pose),
                '-y', str(y_pose),
                '-z', '0.01',
                '-robot_namespace', namespace,
                '-unpause',
            ],
            output='screen'
        )
        spawn_commands.append(spawn_cmd)

        # RViz launch for each robot
        rviz_config_file = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'rviz', 'multi_robot_config.rviz')  # Custom RViz config
        rviz_cmd = Node(
            package='rviz2',
            executable='rviz2',
            namespace=namespace,
            arguments=['-d', rviz_config_file],
            output='screen'
        )
        rviz_commands.append(rviz_cmd)

    # Add spawn commands to the launch description
    for spawn_cmd in spawn_commands:
        ld.add_action(spawn_cmd)

    # Add RViz commands to the launch description
    for rviz_cmd in rviz_commands:
        ld.add_action(rviz_cmd)

    # Load map and start navigation for each robot
    nav2_launch_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'nav2_bringup_launch.py')
    for i in range(num_robots):
        namespace = f'{base_namespace}{i+1}'
        bringup_cmd = ExecuteProcess(
            cmd=['ros2', 'launch', 'nav2_bringup', 'bringup_launch.py', 'map:=', map_file, 'namespace:=', namespace],
            output='screen'
        )
        ld.add_action(bringup_cmd)

    return ld

if __name__ == '__main__':
    # This part can be used to launch the script as a standalone program
    from launch import LaunchService
    ls = LaunchService()
    ls.include_launch_description(generate_launch_description())
    ls.run()
