#!/usr/bin/env python3

import os
import rospy
import cv2
import numpy as np
from duckietown.dtros import DTROS, NodeType
from std_msgs.msg import String

class MyPublisherNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MyPublisherNode, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        # construct publisher
        self.pub = rospy.Publisher('chatter', String, queue_size=10)
      
    
    def run(self):
    #publish message every 1 second
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():    
            cap = cv2.VideoCapture()
            res_w, res_h, fps = 640, 480, 30
            fov = 'full'
            # find best mode
            camera_mode = 3  # 
            # compile gst pipeline
    
            ret, frame = cap.read()
            if frame == None:
                message = "frame is empty"
            else:
                message = "Hello from %s" % os.environ['VEHICLE_NAME']
            
            rospy.loginfo("Publishing message: '%s'" % message)
            self.pub.publish(message)
            rate.sleep()


if __name__ == '__main__':
    # create the node
    node = MyPublisherNode(node_name='my_publisher_node')
    # run node
    node.run()
    # keep spinning
    rospy.spin()

