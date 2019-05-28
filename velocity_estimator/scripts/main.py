#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

class LScan:
    def __init__(self):
        self.rospy=rospy
        self.rospy.init_node('listener',anonymous=True)
        self.rospy.loginfo("Starting Leg Laser")
        # self.initParameters()
        self.initSubscribers()
        self.change=False
        self.run()
    
    # def initParameters(self):
	# 	self.legLaserTopic = self.rospy.get_param("~legLaser_topic","/scan")
	# 	return
    def initSubscribers(self):
        self.subPose = self.rospy.Subscriber("/scan", LaserScan, self.getlaser)
        return
    def initvariables(self):
        self.rate = self.rospy.Rate(100)
        self.angle_min = 0
        self.angle_max = 0
        self.scan_time = 0
        self.ranges = 0
        self.angle_increment = 0
        self.time_increment = 0
        self.range_min = 0
        self.range_max = 0
        self.change = False

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
                print(len(self.ranges))
                self.change=False
        self.rate.sleep()

if __name__ == '__main__':
    try:
        LScan = LScan()
    except rospy.ROSInterruptException:
        pass