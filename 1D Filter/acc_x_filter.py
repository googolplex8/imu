""" from rover_common import aiolcm
from rover_msgs import IMUData

class LinearAccelFilter:
    @attribute threshold
    @attribute weight
    @attribute prev_accel
    @attribute cur_accel

    def __init__(self, threshold, weight):
        self.lcm = aiolcm.AsyncLCM()
        self.lcm.subscribe("/imu")
        
        self.threshold = threshold
        self.weight = weight

    def update(self,prev,cur):
        #thresholding to 0
        if (prev_accel < threshold):
            cur_accel = 0
        #else, perform simple low-pass filtering
        else:
            cur_accel = (weight) * cur_accel + (1-weight) * prev_accel
            prev_accel = cur_accel

        self.lcm.publish('/filtered_imu', self.cur_accel) """




    
