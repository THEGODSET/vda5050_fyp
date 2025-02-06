import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

def robot_list(number_of_robots):
    robots = [
        {'name': 'tb1', 'x_pose': '-1.5', 'y_pose': '-0.5', 'z_pose': 0.01},
        {'name': 'tb2', 'x_pose': '-1.5', 'y_pose': '0.5', 'z_pose': 0.01},
        # {'name': 'tb3', 'x_pose': '1.5', 'y_pose': '-0.5', 'z_pose': 0.01},
        # {'name': 'tb4', 'x_pose': '1.5', 'y_pose': '0.5', 'z_pose': 0.01},
    ]

    return robots[:number_of_robots]  # Return only the first `number_of_robots` entries

def generate_launch_description():
    ld = LaunchDescription()

    #######################
    ### Share Directory ###
    #######################

    TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']
    model_folder = 'turtlebot3_' + TURTLEBOT3_MODEL
    urdf_path = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'models',
        model_folder,
        'model.sdf'
    )

    pkg_turtlebot = get_package_share_directory('turtlebot3_gazebo')
    nav_params_file = os.path.join(pkg_turtlebot, 'params', 'nav2_params.yaml')

    ############################
    ### Launch Configuration ###
    ############################

    map_file = LaunchConfiguration('map_file')
    declare_map_file = DeclareLaunchArgument(
        name='map_file', default_value=os.path.join(pkg_turtlebot, 'map', 'map_maze.yaml'), description='Locate map file'
    )

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    declare_use_sim_time = DeclareLaunchArgument(
        name='use_sim_time', default_value=use_sim_time, description='Use simulator time'
    )

    enable_drive = LaunchConfiguration('enable_drive', default='false')
    declare_enable_drive = DeclareLaunchArgument(
        name='enable_drive', default_value=enable_drive, description='Enable robot drive node'
    )

    enable_rviz = LaunchConfiguration('enable_rviz', default='true')
    declare_enable_rviz = DeclareLaunchArgument(
        name='enable_rviz', default_value=enable_rviz, description='Enable rviz launch'
    )

    rviz_config_file = os.path.join(pkg_turtlebot, 'rviz', 'multi_nav2_default_view.rviz')

    declare_x_pos_cmd = DeclareLaunchArgument(
        'x_pose', default_value='0.0', description='X position of the robot')
    declare_y_pos_cmd = DeclareLaunchArgument(
        'y_pose', default_value='0.0', description='Y position of the robot')

    robots = robot_list(2)  # Adjust the number of robots here

    spawn_robots_cmds = []

    for robot in robots:
        namespace = '/' + robot['name']
        spawn_robots_cmds.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(pkg_turtlebot, 'launch',
                                                           'spawn_multiple_entity_with_nav.launch.py')),
                launch_arguments={
                                  'entity': TURTLEBOT3_MODEL,
                                  'file': urdf_path,
                                  'x': str(robot['x_pose']),
                                  'y': str(robot['y_pose']),
                                  'robot_name': robot['name'],
                                  'robot_namespace': namespace,
                                  'use_sim_time': 'true',
                                  'map_file': map_file,
                                  'nav_params_file': nav_params_file,
                                  'rviz_config_file': rviz_config_file,
                                  }.items()))

    for spawn_robot_cmd in spawn_robots_cmds:
        ld.add_action(spawn_robot_cmd)

    ld.add_action(declare_x_pos_cmd)
    ld.add_action(declare_y_pos_cmd)
    ld.add_action(declare_use_sim_time)
    ld.add_action(declare_enable_drive)
    ld.add_action(declare_enable_rviz)

    return ld
