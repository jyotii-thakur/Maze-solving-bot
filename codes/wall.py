#!/usr/bin/env python3
from math import inf
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
import time

a=0
b=[]

def update(data):
    global a,b
    p = data
    a = min(p.ranges[49:89])
    b = p.ranges[49:89]
def goal():
    global a,b
    m=a
    print(m)
    v=20
    w=-20
    while not rospy.is_shutdown():
        check = b.count(inf)
        if( m-0.3 <= a <= m+0.3):
            j1.publish(v)
            j2.publish(w)
            j3.publish(v)
            j4.publish(w)
  
        elif(a > m + 0.3 and check>25): 
            print("a")  
            j1.publish(v)
            j2.publish(v)
            j3.publish(v)
            j4.publish(v)

        elif(a < m - 0.3 ): 
            print("b")  
            j1.publish(w)
            j2.publish(w)
            j3.publish(w)
            j4.publish(w)

        else:
            print("c")
            j1.publish(v)
            j2.publish(w)
            j3.publish(v)
            j4.publish(w)
     


   

if __name__ == "__main__":
    try:
        rospy.init_node("kaam", anonymous=True)
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
