from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sza_xui_kordinata',
            executable='coordinate_publisher',
            output='screen'
        ),
        Node(
            package='sza_xui_kordinata',
            executable='distance_subscriber',
            output='screen'
        ),
    ])