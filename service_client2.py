#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import multiply

def callback(data):
    rospy.loginfo("Multiplication of %d with the sum %d is %d.",data.c,data.z,data.d)
    
def client_2():


    rospy.init_node('client_2', anonymous=True)

    rospy.Subscriber("chatter", multiply, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    client_2()
