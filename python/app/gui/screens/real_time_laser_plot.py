import json
import os

os.environ['ROS_MASTER_URI'] = 'http://10.4.38.11:11311'
os.environ['ROS_MASTER_IP'] = '10.4.38.11'
os.environ['ROS_IP'] = '10.4.38.10'

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


#! /usr/bin/env python
import rospy
from std_msgs.msg import String



class Visualiser:

    def __init__(self):
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': 'polar'})
        mgr = plt.get_current_fig_manager()
        mgr.window.wm_geometry("+0+0") # move the window
        mgr.window.title("Monitor Laser en tiempo real")

        self.fig.set_size_inches(4, 4, forward=True)

        self.ln, = plt.plot([], [], 'g.')
        self.max_r = 5

    def plot_init(self):
        self.ax.set_rlim(0, self.max_r)
        return self.ln 

    def update_plot(self, frame):
        self.ax.clear()
        self.ax.set_theta_direction(1)
        self.ax.set_rlim(0, self.max_r)
        self.ax.scatter(self.angles, self.ranges, s=1, c='r')
        return self.ln
    
    def callback(self, msg):
        scan = json.loads(msg.data)
        #print(scan)
        self.ranges = scan['ranges']
        self.angles = np.linspace(-np.pi, np.pi, num=len(self.ranges))
        



def run():
    rospy.init_node('scan_values_receiver')
    vis = Visualiser()
    sub = rospy.Subscriber('/scan_json', String, vis.callback)
    ani = FuncAnimation(vis.fig, vis.update_plot, init_func=vis.plot_init)
    plt.show(block=True) 
    #rospy.spin()

if __name__ == '__main__':
    run()



