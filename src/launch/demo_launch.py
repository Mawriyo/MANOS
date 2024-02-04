from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='castelet',
            executable='castelet',
            name='castelet_node',
            output='screen'
        ),
        Node(
            package='camera',
            executable='camera',
            name='camera_node',
            output='screen'
        ),
        Node(
            package='hand_detector',
            executable='hand_detector',
            name='hand_detector_node',
            output='screen'
        ),
        Node(
            package='host_listener_package',
            executable='host_listener',
            name='host_listener_node',
            output='screen'
        ),
        Node(
            package='manos_manager',
            executable='manos_manager',
            name='manos_manager_node',
            output='screen'
        )

    ])

