#!/usr/bin/env python

import os, time, logging
os.environ['ROS_MASTER_URI'] = 'http://172.20.10.2:11311'
os.environ['ROS_MASTER_IP'] = '172.20.10.2'
os.environ['ROS_IP'] = '172.20.10.4'

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class RobotController:
    rospy.init_node('robot_controller', anonymous=True)
    def __init__(self):
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.velocity = 0.5
        self.angular_velocity = 1

    def getVelocity(self):
        return self.velocity
    
    def setVelocity(self, velocity):
        self.velocity = velocity

    def moveUp(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.velocity
        self.velocity_publisher.publish(vel_msg)

    def moveDown(self):
        vel_msg = Twist()
        vel_msg.linear.x = - self.velocity
        self.velocity_publisher.publish(vel_msg)

    def moveLeft(self):
        vel_msg = Twist()
        vel_msg.linear.y = self.velocity
        self.velocity_publisher.publish(vel_msg)

    def moveRight(self):
        vel_msg = Twist()
        vel_msg.linear.y = - self.velocity
        self.velocity_publisher.publish(vel_msg)

    def moveUpLeft(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.velocity
        vel_msg.angular.z = self.angular_velocity
        self.velocity_publisher.publish(vel_msg)

    def moveUpRight(self):
        vel_msg = Twist()
        vel_msg.linear.x = self.velocity
        vel_msg.angular.z = - self.angular_velocity
        self.velocity_publisher.publish(vel_msg)

    def moveDownLeft(self):
        vel_msg = Twist()
        vel_msg.linear.x = - self.velocity
        vel_msg.angular.z = - self.angular_velocity
        self.velocity_publisher.publish(vel_msg)

    def moveDownRight(self):
        vel_msg = Twist()
        vel_msg.linear.x = - self.velocity
        vel_msg.angular.z =  self.angular_velocity
        self.velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    rc = RobotController()
    time.sleep(1)
    rc.moveUp()