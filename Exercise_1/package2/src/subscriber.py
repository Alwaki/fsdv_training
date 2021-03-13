#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

class Listener:
    """Object which performs publishing and subscribtion"""
    def __init__(self):
        """Publisher and subscriber attributes"""
        rospy.init_node("nodeB", anonymous=True)
        self.sub = rospy.Subscriber("wallen_kiessling", Float32, self.callback, queue_size=1)
        self.pub = rospy.Publisher("/kthfs/result", Float32, queue_size=1)
    
    def callback(self, data):
        """Performs multiplication on given data and publishes result"""
        number = data.data * 0.15
        self.pub.publish(number)

if __name__ == '__main__':
    try:
        sub = Listener()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

