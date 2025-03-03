import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, RegisterEventHandler, IncludeLaunchDescription, ExecuteProcess, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.event_handlers import OnProcessExit
from launch.conditions import IfCondition
from launch_ros.actions import Node

def initial_pose_cmd(context):
    # Resolve LaunchConfigurations
    x_pose = LaunchConfiguration('x_pose').perform(context)
    y_pose = LaunchConfiguration('y_pose').perform(context)
    namespace = LaunchConfiguration('namespace').perform(context)

    message = '{header: {frame_id: map}, pose: {pose: {position: {x: ' + \
    f'{x_pose}, y: {y_pose}' + \
    ', z: 0.1}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0000000}}, }}'

    command = ['ros2', 'topic', 'pub', '-t', '3', '--qos-reliability', 'reliable', f'{namespace}/initialpose',
            'geometry_msgs/PoseWithCovarianceStamped', '"', message, '"']

    # Print resolved values
    return [
        ExecuteProcess(
            cmd=command,
            output='screen',
            shell=True
            )
    ]

def generate_launch_description():
    ld = LaunchDescription()

    package_dir = get_package_share_directory('turtlebot3_gazebo')
    nav_launch_dir = os.path.join(package_dir, 'launch', 'nav2_bringup')
    map_file = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'map','map_maze.yaml')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    declare_use_sim_time = DeclareLaunchArgument(
        name='use_sim_time', default_value=use_sim_time, description='Use simulator time'
    )

    namespace = LaunchConfiguration('namespace', default='')
    x_pose = LaunchConfiguration('x_pose', default='0.0')
    y_pose = LaunchConfiguration('y_pose', default='0.0')

    enable_drive = LaunchConfiguration('enable_drive', default='false')
    declare_enable_drive = DeclareLaunchArgument(
        name='enable_drive', default_value=enable_drive, description='Enable robot drive node'
    )

    enable_rviz = LaunchConfiguration('enable_rviz', default='true')
    declare_enable_rviz = DeclareLaunchArgument(
        name='enable_rviz', default_value=enable_rviz, description='Enable rviz launch'
    )

    params_file = LaunchConfiguration('nav_params_file')
    declare_params_file_cmd = DeclareLaunchArgument(
        'nav_params_file',
        default_value=os.path.join(package_dir, 'params', 'nav2_params.yaml'),
        description='Full path to the ROS2 parameters file to use for all launched nodes')
    
    rviz_config_file = LaunchConfiguration('rviz_config_file')
    declare_rviz_config_file_cmd = DeclareLaunchArgument(
        'rviz_config_file',
        default_value=os.path.join(
            package_dir, 'rviz', 'multi_nav2_default_view.rviz'),
        description='Full path to the RVIZ config file to use')
    
    ld.add_action(declare_use_sim_time)
    ld.add_action(declare_enable_drive)
    ld.add_action(declare_enable_rviz)
    ld.add_action(declare_params_file_cmd)
    ld.add_action(declare_rviz_config_file_cmd)

    remappings = [('/tf', 'tf'), ('/tf_static', 'tf_static')]

    TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']
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
    assert os.path.exists(urdf_path), "Turtlebot.urdf doesnt exist in "+str(urdf_path)
    
    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read().strip()

    last_action = None

    # print(f"SDF Path: {sdf_path}")
    # print(f"URDF Path: {urdf_path}")

    map_server_node = Node(
        package='nav2_map_server',
        executable='map_server',
        output='screen',
        parameters=[{
            'yaml_filename': map_file,
            'use_sim_time': use_sim_time
        }],
        remappings=remappings
    )

    turtlebot_state_publisher = Node(
        package='robot_state_publisher',
        # namespace=namespace,
        name='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time,
                    'robot_description': robot_desc}],
        remappings=remappings,
        arguments=[urdf_path],
    )
    
    spawn_turtlebot3_burger = Node(package='gazebo_ros', executable='spawn_entity.py',arguments=[
        '-entity', namespace,
        '-file', sdf_path,
        '-x', x_pose,
        '-y', y_pose,
        '-z', '0.01',
        '-robot_namespace', namespace,
        '-unpause',
        ], output='screen')
    
    bringup_cmd = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav_launch_dir, 'bringup_launch.py')),
                launch_arguments={
                                'slam': 'False',
                                'namespace': namespace,
                                'use_namespace': 'True',
                                'map': map_file,
                                'map_server': 'False',
                                'params_file': params_file,
                                'default_bt_xml_filename': os.path.join(
                                    get_package_share_directory('nav2_bt_navigator'),
                                    'behavior_trees', 'navigate_w_replanning_and_recovery.xml'),
                                'autostart': 'true',
                                'use_sim_time': use_sim_time, 'log_level': 'warn'}.items()
                                )
    
    if last_action is None:
        # Call add_action directly for the first robot to facilitate chain instantiation via RegisterEventHandler
        ld.add_action(turtlebot_state_publisher)
        ld.add_action(spawn_turtlebot3_burger)
        ld.add_action(bringup_cmd)

    else:
        # Use RegisterEventHandler to ensure next robot creation happens only after the previous one is completed.
        # Simply calling ld.add_action for spawn_entity introduces issues due to parallel run.
        spawn_turtlebot3_event = RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=last_action,
                on_exit=[spawn_turtlebot3_burger,
                        turtlebot_state_publisher,
                        bringup_cmd],
            )
        )

        ld.add_action(spawn_turtlebot3_event)

    last_action = spawn_turtlebot3_burger

    rviz_cmd = ExecuteProcess(
        cmd=['gzclient'],
        output='screen',
        shell=True
    )

    # rviz_cmd = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join(nav_launch_dir, 'rviz_launch.py')),
    #         launch_arguments={'use_sim_time': use_sim_time, 
    #                             'namespace': namespace,
    #                             'use_namespace': 'true',
    #                             'rviz_config': rviz_config_file,
    #                             'log_level': 'warn'}.items(),
    #                             condition=IfCondition(enable_rviz)
    #                             )

    drive_turtlebot3_burger = Node(
        package='turtlebot3_gazebo', executable='turtlebot3_drive',
        namespace=namespace, output='screen',
        condition=IfCondition(enable_drive),
    )

    # Use RegisterEventHandler to ensure next robot rviz launch happens 
    # only after all robots are spawned
    post_spawn_event = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=last_action,
            on_exit=[
                # rviz_cmd,
                drive_turtlebot3_burger],
        )
    )

    # last_action = initial_pose_cmd
    # ld.add_action(map_server_node)
    ld.add_action(post_spawn_event)
    ld.add_action(OpaqueFunction(function=initial_pose_cmd))

    return ld