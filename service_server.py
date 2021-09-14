#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import add , addResponse


def callback(request):
    return addResponse(request.a + request.b)
   

def addition():
    rospy.init_node("server")
    service = rospy.Service("server",add,callback)
    rospy.spin()


if __name__ == '__main__':
    addition()
