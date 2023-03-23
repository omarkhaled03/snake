import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command, PathJoinSubstitution

def generate_launch_description():

    pkg_path = os.path.join(get_package_share_directory('snake'))

    xacro_file = os.path.join(pkg_path,'urdf/','snake_robot_core.xacro')
    robot_description_config = xacro.process_file(xacro_file)   
    
    robot_desc = robot_description_config.toxml()



    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),

        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            parameters=[
                {"robot_description": robot_desc}],
            output="screen"),

    ])




