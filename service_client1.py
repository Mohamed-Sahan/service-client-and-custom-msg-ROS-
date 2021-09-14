#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import add, addResponse
from beginner_tutorials.msg import multiply

def client_1(x,y):
    rospy.init_node("client_1",anonymous=True)
    rospy.wait_for_service("server")
    rate = rospy.Rate(1) 
    while not rospy.is_shutdown():
        add_two_ints = rospy.ServiceProxy("server",add)
        response = add_two_ints(x,y)
        rospy.loginfo("Sum of %d and %d is %d.",x,y,response.result)

        pub = rospy.Publisher('chatter', multiply, queue_size=10)
        msg = multiply()
        msg.z = response.result
        msg.c = 4
        msg.d = msg.z * msg.c
    
    
        pub.publish(msg)
        rate.sleep()
    

if __name__ == '__main__':
    client_1(2,3)
