#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

class LScan():
    def __init__(self):
        self.rospy=rospy
        self.change=False
        self.rate = self.rospy.Rate(100)
        self.value=0
        self.rospy.init_node('listener',anonymous=True)
        self.rospy.Subscriber("~scan_legs","/scan",LaserScan,self.getlaser)
        self.run()

    def getlaser(self,msg):
        self.angle_min = msg.angle_min
        self.angle_max =msg.angle_max
        self.time_increment = msg.time_increment
        self.scan_time = msg.scan_time 
        self.range_min =msg.range_min 
        self.range_max =msg.range_max 
        self.ranges=msg.ranges
        self.intensities = msg.intensities
        self.change=True

    def run(self):        
        while not self.rospy.is_shutdown():
            self.msg=LaserScan()
            if(self.change):
                print(self.ranges)
                self.change=False
        self.rate.sleep()

if __name__ == '__main__':
    try:
        LS=LScan()
    except rospy.ROSInterruptException:
        pass