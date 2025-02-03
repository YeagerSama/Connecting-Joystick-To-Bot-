from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    myJoyNode=Node(package="ninja",
                   executable="currentJoys",
                   name="Joystick_Controller",
                   )
    
    existingJoy=Node(package="joy",
                   executable="joy_node",
                   name="joy_node",
                   )
    
    Turtle=Node(package="turtlesim",
                   executable="turtlesim_node",
                   name="turtlesim_node",
                   )
    
    
    return LaunchDescription([Turtle,myJoyNode,existingJoy])