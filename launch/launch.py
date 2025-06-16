from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
 
def generate_launch_description():
    return LaunchDescription([
        # Lançar o Gazebo com o modelo
        ExecuteProcess(
            cmd=[
                'ign', 'gazebo',
                '/home/kifelix/ros2_ws/src/robo_3/model/robo3.sdf',
                '--verbose'
            ],
            output='screen'
        ),
 
        # Ponte /cmd_vel (Twist)
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist'],
            output='screen'
        ),
 
        # Ponte /imu
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/imu@sensor_msgs/msg/Imu@ignition.msgs.IMU'],
            output='screen'
        ),
 
    ])
