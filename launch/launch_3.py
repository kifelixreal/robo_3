'''
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
        # Ponte para a imagem da câmera
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/camera_rgb/image_raw@sensor_msgs/msg/Image@ignition.msgs.Image'],
            output='screen'
        ),

        # Ponte para as informações da câmera (calibração, etc.)
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/camera_rgb/camera_info@sensor_msgs/msg/CameraInfo@ignition.msgs.CameraInfo'],
            output='screen'
        ), 
    ])
'''
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
 
def generate_launch_description():
    return LaunchDescription([
        # Lançar o Gazebo com o modelo
        ExecuteProcess(
            cmd=[
                'ign', 'gazebo',
                '/home/kifelix/ros2_ws/src/robo_3/model/robo3.sdf', # Caminho atualizado
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
        # --- PONTES PARA A CÂMERA RGB (CONFIGURAÇÃO OTIMIZADA COM BASE NO `ign topic -l`) ---
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                # Pega dados de '/camera_rgb/image_raw' (Ignition) e publica em '/camera_rgb/image_raw' (ROS 2)
                # Formato: "ROS2_TOPIC@ROS2_MSG_TYPE@IGNITION_MSG_TYPE"
                # Se o nome do tópico Ignition for o mesmo do ROS 2, não precisa de remapping explícito aqui.
                '/camera@sensor_msgs/msg/Image@ignition.msgs.Image',
                
                # Pega dados de '/camera_rgb/camera_info' (Ignition) e publica em '/camera_rgb/camera_info' (ROS 2)
                'camera_info@sensor_msgs/msg/CameraInfo@ignition.msgs.CameraInfo'
            ],
            # Remova a seção 'remappings' para a câmera, pois os nomes já batem!
            # remappings=[
            #     ('/camera_rgb/image_raw', '/camera_rgb/image_raw'),
            #     ('/camera_rgb/camera_info', '/camera_rgb/camera_info')
            # ],
            output='screen'
        ),
        # --- FIM DAS PONTES ---
    ])