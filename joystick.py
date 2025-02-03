#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class Joystick_Controller(Node):

    def __init__(self):
        super().__init__("Joystick_Controller")
        #create_subscription( Message type, Topic Name, Callback function, QoS). A callback function is required to process incoming messages.
        self.getVel=self.create_subscription(Joy,"/joy",self.listener_callback,10)
        #publisher does not require a callback because it does not process any incoming data.
        self.giveVel=self.create_publisher(Twist,"/turtle1/cmd_vel",10)

    def listener_callback(self,data:Joy): # cux data  of joy type and self object both inputs are required
        msg=Twist()
        msg.linear.y=data.axes[0]*2.0
        msg.linear.x=data.axes[1]*4.0
        if data.axes[3]<(-0.5) or data.axes[3]>0.0 :
          msg.angular.z=data.axes[3]
        self.giveVel.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    MyObject=Joystick_Controller()

    rclpy.spin(MyObject)
    rclpy.shutdown()

if __name__=="__main__":
    main()