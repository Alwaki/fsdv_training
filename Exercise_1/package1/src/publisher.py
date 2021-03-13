#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def talker():
    """Publishes an increasing number at rate 20 Hz"""
    rospy.init_node('nodeA', anonymous=True)
    pub = rospy.Publisher('wallen_kiessling', Float32, queue_size=1)
    rate = rospy.Rate(20)
    n = 0

    while not rospy.is_shutdown():
        pub.publish(n)
        rospy.loginfo(n)
        n = n + 4
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
