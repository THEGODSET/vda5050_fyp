import sys
import os

from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def robot_list(number_of_robots):

    robots = []

    for i in range(number_of_robots):
        robot_name = "turtlebot" + str(i)
        x_pos = float(i) * 2.0
        # y_pos = float(i) * 2.0
        robots.append({'name': robot_name, 'x_pose': x_pos, 'y_pose': 1.0, 'z_pose': 0.01})

    return robots

def generate_launch_description():
    # Get the urdf file
    TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']
    model_folder = 'turtlebot3_' + TURTLEBOT3_MODEL
    urdf_path = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'models',
        model_folder,
        'model.sdf'
    )
    pkg_turtlebot = get_package_share_directory('turtlebot3_gazebo')

    declare_x_pos_cmd = DeclareLaunchArgument(
        'x_pose', default_value='0.0', description='X position of the robot')
    declare_y_pos_cmd = DeclareLaunchArgument(
        'y_pose', default_value='0.0', description='Y position of the robot')

    robots = robot_list(1)

    spawn_robots_cmds = []

    print(str(robots))
    for robot in robots:
        print("#############"+str(robot))
        spawn_robots_cmds.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(pkg_turtlebot, 'launch',
                                                           'spawn_multiple_entity.launch.py')),
                launch_arguments={
                                  'entity': TURTLEBOT3_MODEL,
                                  'file': urdf_path,
                                  'x': str(robot['x_pose']),
                                  'y': str(robot['y_pose']),
                                  'robot_name': robot['name'],
                                  'robot_namespace': robot['name'],
                                  }.items()))

    ld = LaunchDescription()

    for spawn_robot_cmd in spawn_robots_cmds:
        ld.add_action(spawn_robot_cmd)
        
    ld.add_action(declare_x_pos_cmd)
    ld.add_action(declare_y_pos_cmd)

    # # Declare the launch options
    # ld.add_action(declare_x_position_cmd)
    # ld.add_action(declare_y_position_cmd)

    # # Add any conditioned actions
    # ld.add_action(start_gazebo_ros_spawner_cmd)

    return ld
