import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command, PathJoinSubstitution
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
import xacro
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command, PathJoinSubstitution

def generate_launch_description():
    package_name='snake'
    gazebo_spwan = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','spwan.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')])             )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'snake_robot'],
                        output='screen')

    robot_controller_spawner1 = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joints1_controllers", "-c", "/controller_manager"],
    )

    robot_controller_spawner2 = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joints2_controllers", "-c", "/controller_manager"],
    )

    robot_controller_spawner3 = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joints3_controllers", "-c", "/controller_manager"],
    )

    robot_controller_spawner4 = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joints4_controllers", "-c", "/controller_manager"],
    )

    robot_controller_spawner5 = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joints5_controllers", "-c", "/controller_manager"],
    )

    robot_controller_spawner6 = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joints6_controllers", "-c", "/controller_manager"],
    )
    robot_controller_spawner7 = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joints7_controllers", "-c", "/controller_manager"],
    )

    robot_controller_spawner8 = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joints8_controllers", "-c", "/controller_manager"],
    )

    robot_controller_spawner9 = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joints9_controllers", "-c", "/controller_manager"],
    )



    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )

    return LaunchDescription([
        RegisterEventHandler(
        event_handler= OnProcessExit(
        target_action=joint_state_broadcaster_spawner,
        on_exit = [robot_controller_spawner1,robot_controller_spawner2,robot_controller_spawner3,
                   robot_controller_spawner4,robot_controller_spawner5,robot_controller_spawner6,
                   robot_controller_spawner7,robot_controller_spawner8,robot_controller_spawner9]
        )),
        gazebo,
        gazebo_spwan,
        spawn_entity,
        joint_state_broadcaster_spawner,
      ])

