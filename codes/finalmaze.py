#!/usr/bin/env python3
from math import inf
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
import time




a=b=0


def update(data):
    global a,b
    p = data
    a = min(p.ranges[60:120])
    b = min(p.ranges[70:110])
  

    
        
def goal():
    global a,b
    m=a
    while(not rospy.is_shutdown()):
        v = 5000
        w = -5000
        if(m-0.1<=a<=m+0.3 and b>1.3):
            print("a")
            j1.publish(v)
            j2.publish(w)
            j3.publish(v)
            j4.publish(w)
             
        elif(a>m+0.3 and b>1.3):
            print("b")
            j1.publish(v)
            j2.publish(v)
            j3.publish(v)
            j4.publish(v)
        
        elif(b<1.3 and a<m):
            print("c")
            j1.publish(w)
            j2.publish(w)
            j3.publish(w)
            j4.publish(w)
    
        elif(b<1.3):
            print("d")
            j1.publish(w)
            j2.publish(w)
            j3.publish(w)
            j4.publish(w)


        else:
            print("e")
            j1.publish(v)
            j2.publish(w)
            j3.publish(v)
            j4.publish(w)

if __name__ == "__main__":
    try:
        rospy.init_node("finalkaam", anonymous=True)
        j1 = rospy.Publisher('joint1_vel_controller/command',Float64,queue_size=10)
        j2 = rospy.Publisher('joint2_vel_controller/command',Float64,queue_size=10)
        j3 = rospy.Publisher('joint3_vel_controller/command',Float64,queue_size=10)
        j4 = rospy.Publisher('joint4_vel_controller/command',Float64,queue_size=10)
        pos = rospy.Subscriber('/laser/scan',LaserScan,update)
        time.sleep(2)
        p = LaserScan()
        goal()
        

    except rospy.ROSInterruptException:
        pass