#!/usr/bin/env python3
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    launch_file_dir = get_package_share_directory('turtlebot3_gazebo')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    # map_file = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'map','map_maze.yaml')

    x_pose = LaunchConfiguration('x_pose', default='-17.0')
    y_pose = LaunchConfiguration('y_pose', default='-23.0')

    world = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'worlds',
        'office.world'
    )

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = ExecuteProcess(
            cmd=['gzclient'],
            output='screen',
            shell=True
        )
    
    # remappings = [('/tf', 'tf'),
    #               ('/tf_static', 'tf_static'),
    #               ('/scan', 'scan')]

    # map_server=Node(package='nav2_map_server',
    #     executable='map_server',
    #     name='map_server',
    #     output='screen',
    #     parameters=[{'yaml_filename': os.path.join(map_file),
    #                  },],
    #     remappings=remappings
    #     )

    # map_server_lifecyle=Node(package='nav2_lifecycle_manager',
    #         executable='lifecycle_manager',
    #         name='lifecycle_manager_map_server',
    #         output='screen',
    #         parameters=[{'use_sim_time': use_sim_time},
    #                     {'autostart': True},
    #                     {'node_names': ['map_server']}])

    spawn_turtlebot_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'launch','spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': x_pose,
            'y_pose': y_pose
        }.items()
    )

    ld = LaunchDescription()

    # Add the commands to the launch description
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)
    ld.add_action(spawn_turtlebot_cmd)
    # ld.add_action(map_server)
    # ld.add_action(map_server_lifecyle)

    return ld
