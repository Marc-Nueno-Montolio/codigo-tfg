#! /usr/bin/env python
import os
import json
os.environ['ROS_MASTER_URI']='http://10.4.38.13:11311'
os.environ['ROS_IP']='10.4.38.13'
from datetime import datetime
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

def callback(msg):
    scan={
        'header':{
            'seq':msg.header.seq,
            'stamp':{
                'secs': msg.header.stamp.secs,
                'nsecs': msg.header.stamp.nsecs
            },
            'frame_id': msg.header.frame_id
        },
        'angle_min': msg.angle_min,
        'angle_max': msg.angle_max,
        'time_increment': msg.time_increment,
        'scan_time': msg.scan_time,
        'range_min': msg.range_min,
        'range_max': msg.range_max,
        'ranges': msg.ranges,
        'intensities' : msg.intensities
    }
    print(scan['header'])
    pub.publish(json.dumps(scan, indent=4))
rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('scan_json', String)
rospy.spin()
