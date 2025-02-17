"""Launch Gazebo server and client with command line arguments."""
#"""Spawn robot from URDF file."""
#https://gist.github.com/rfzeg/63d824f0c6ed44da639e9630a76fbc6c

import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration

os.environ['GZ_SIM_RESOURCE_PATH'] = \
    os.path.join( get_package_share_directory('gz_rcll_models'),
        'worlds'
    ) + \
    os.pathsep + os.path.join(
        get_package_share_directory('gz_rcll_models'),
        'models'
    )
print(os.environ['GZ_SIM_RESOURCE_PATH'])

def generate_launch_description():
    #use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    verbose = LaunchConfiguration('v', default='1')
    #robot_name = 'rrbot_description'
    gz_rcll_launch_arg = DeclareLaunchArgument(
        'v',
        default_value='1'
    )

    world_file_name = 'rcll-default.sdf'
    

    world = os.path.join(
        get_package_share_directory('gz_rcll_models'),
        'worlds',
        world_file_name
    )

    #urdf = os.path.join(get_package_share_directory(
    #    'gz_rcll_models'), 'urdf', 'my_robot.urdf')

    #xml = open(urdf, 'r').read()

    #xml = xml.replace('"', '\\"')

    #spawn_args = '{name: \"my_robot\", xml: \"' + xml + '\" }'

    return LaunchDescription([
        gz_rcll_launch_arg,
        ExecuteProcess(
            cmd=['gz', 'sim', '-v', verbose, world_file_name],
            output='screen'),

        #ExecuteProcess(
        #    cmd=['ros2', 'param', 'set', '/gazebo',
        #         'use_sim_time', use_sim_time],
        #    output='screen'),

        #ExecuteProcess(
        #    cmd=['ros2', 'service', 'call', '/spawn_entity',
        #         'gazebo_msgs/SpawnEntity', swpan_args],
        #    output='screen'),
    ]) 
