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
        {'name': 'tb3', 'x_pose': '1.5', 'y_pose': '-0.5', 'z_pose': 0.01},
        {'name': 'tb4', 'x_pose': '1.5', 'y_pose': '0.5', 'z_pose': 0.01},
        ]

    # for i in range(number_of_robots):
    #     robot_name = "turtlebot" + str(i)
    #     x_pos = float(i) * 2.0
    #     # y_pos = float(i) * 2.0
    #     robots.append({'name': robot_name, 'x_pose': x_pos, 'y_pose': 1.0, 'z_pose': 0.01})

    return robots

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

    # nav_launch_dir = os.path.join(pkg_turtlebot, 'launch', 'nav2_bringup')
    nav_params_file = os.path.join(pkg_turtlebot, 'params','nav2_params.yaml')

    ############################
    ### Launch Configuration ###
    ############################

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


    # declare_rviz_config_file_cmd = DeclareLaunchArgument(
    #     'rviz_config_file',
    #     default_value=os.path.join(
    #         pkg_turtlebot, 'rviz', 'multi_nav2_default_view.rviz'),
    #     description='Full path to the RVIZ config file to use')
    
    #################
    ### Arguments ###
    #################

    declare_x_pos_cmd = DeclareLaunchArgument(
        'x_pose', default_value='0.0', description='X position of the robot')
    declare_y_pos_cmd = DeclareLaunchArgument(
        'y_pose', default_value='0.0', description='Y position of the robot')

    robots = robot_list(1)

    spawn_robots_cmds = []

    # print(str(robots))

    # last_action = None

    for robot in robots:
        namespace = '/' + robot['name']
        spawn_launch = spawn_robots_cmds.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(pkg_turtlebot, 'launch',
                                                           'spawn_multiple_entity.launch.py')),
                launch_arguments={
                                  'entity': TURTLEBOT3_MODEL,
                                  'file': urdf_path,
                                  'x': str(robot['x_pose']),
                                  'y': str(robot['y_pose']),
                                  'robot_name': robot['name'],
                                  'robot_namespace': namespace,
                                  'nav_params_file': nav_params_file,
                                  'rviz_config_file': rviz_config_file,
                                  }.items()))
        
        # spawn_turtlebot3_event = RegisterEventHandler(
        #     event_handler=OnProcessExit(
        #         target_action=last_action,
        #         on_exit=[spawn_launch],
        #     )
        # )
        
        # ld.add_action(spawn_turtlebot3_event)




    # Use RegisterEventHandler to ensure next robot rviz launch happens 
    # only after all robots are spawned
    # post_spawn_event = RegisterEventHandler(
    #     event_handler=OnProcessExit(
    #         target_action=last_action,
    #         on_exit=[initial_pose_cmd, rviz_cmd, drive_turtlebot3_burger],
    #     )
    # )

    # Perform next rviz and other node instantiation after the previous intialpose request done
    # last_action = initial_pose_cmd

    # ld.add_action(post_spawn_event)

    for spawn_robot_cmd in spawn_robots_cmds:
        ld.add_action(spawn_robot_cmd)
        
    ld.add_action(declare_x_pos_cmd)
    ld.add_action(declare_y_pos_cmd)
    ld.add_action(declare_use_sim_time)
    ld.add_action(declare_enable_drive)
    ld.add_action(declare_enable_rviz)
    # ld.add_action(declare_rviz_config_file_cmd)



    return ld
