import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, RegisterEventHandler, IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.event_handlers import OnProcessExit
from launch.conditions import IfCondition
from launch_ros.actions import Node


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    pkg_turtlebot = get_package_share_directory('turtlebot3_gazebo')
    nav_launch_dir = os.path.join(pkg_turtlebot, 'launch', 'nav2_bringup')

    DeclareLaunchArgument(
    'use_sim_time',
    default_value='false',
    description='Use simulation (Gazebo) clock if true')

    enable_drive = LaunchConfiguration('enable_drive', default='false')

    enable_rviz = LaunchConfiguration('enable_rviz', default='true')
    declare_enable_rviz = DeclareLaunchArgument(
        name='enable_rviz', default_value=enable_rviz, description='Enable rviz launch'
    )

    remappings = [('/tf', 'tf'), ('/tf_static', 'tf_static')]

    TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']
    model_folder = 'turtlebot3_' + TURTLEBOT3_MODEL
    urdf_path = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'models',
        model_folder,
        'model.sdf'
    )
    assert os.path.exists(urdf_path), "Turtlebot.urdf doesnt exist in "+str(urdf_path)
    
    params_file = LaunchConfiguration('nav_params_file')

    rviz_config_file = LaunchConfiguration('rviz_config_file')
    
    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    turtlebot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=LaunchConfiguration('robot_namespace'),
        output='screen',
        parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}],
        remappings=remappings,
        arguments=[urdf_path])
    
    spawn_turtlebot3_burger = Node(package='gazebo_ros', executable='spawn_entity.py', arguments=[
        '-entity', LaunchConfiguration('robot_name'),
        '-file', urdf_path,
        '-x', LaunchConfiguration('x'),
        '-y', LaunchConfiguration('y'),
        '-z', '0.01',
        '-robot_namespace', LaunchConfiguration('robot_namespace'),
        '-unpause',
        ], output='screen')
    
    bringup_cmd = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
        os.path.join(nav_launch_dir, 'bringup_launch.py')),
        launch_arguments={  
                        'slam': 'False',
                        'namespace': LaunchConfiguration('robot_namespace'),
                        'use_namespace': 'True',
                        'map': '',
                        'map_server': 'False',
                        'params_file': params_file,
                        'default_bt_xml_filename': os.path.join(
                            get_package_share_directory('nav2_bt_navigator'),
                            'behavior_trees', 'navigate_w_replanning_and_recovery.xml'),
                        'autostart': 'true',
                        'use_sim_time': use_sim_time, 'log_level': 'warn'}.items()
                        )

    x_pose = str(LaunchConfiguration('x', default='-2.0'))
    y_pose = str(LaunchConfiguration('y', default='-0.5'))
    message = '{"header": {"frame_id": "map"}, "pose": {"pose": {"position": {"x": ' + \
    x_pose + ', "y": ' + y_pose + \
    ', "z": 0.1}, "orientation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0}}}}'


    initial_pose_cmd = ExecuteProcess(
        cmd=['ros2', 'topic', 'pub', '-t', '3', '--qos-reliability', 'reliable', str(LaunchConfiguration('namespace')) + '/initialpose',
            'geometry_msgs/PoseWithCovarianceStamped', message],
        output='screen'
    )

    rviz_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav_launch_dir, 'rviz_launch.py')),
            launch_arguments={'use_sim_time': use_sim_time, 
                                'namespace': LaunchConfiguration('namespace'),
                                'use_namespace': 'True',
                                'rviz_config': rviz_config_file, 'log_level': 'warn'}.items(),
                                condition=IfCondition(enable_rviz)
                                )

    drive_turtlebot3_burger = Node(
        package='turtlebot3_gazebo', executable='turtlebot3_drive',
        namespace=LaunchConfiguration('namespace'), output='screen',
        condition=IfCondition(enable_drive),
    )

    ld = LaunchDescription()

    ld.add_action(turtlebot_state_publisher)
    ld.add_action(spawn_turtlebot3_burger)
    ld.add_action(bringup_cmd)
    ld.add_action(initial_pose_cmd)
    ld.add_action(rviz_cmd)
    ld.add_action(drive_turtlebot3_burger)
    ld.add_action(declare_enable_rviz)


    return ld