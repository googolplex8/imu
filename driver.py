import smbus
import time as t
import numpy as np
from madgwickahrs import MadgwickAHRS

I2C_IMU_ADDRESS = 0x69
bus = smbus.SMBus(2)

filter = MadgwickAHRS()

def get_decimal(ls, ms):
    high = read_data(ms) << 8
    return np.int16((high | read_data(ls)))

def read_data(num):
    a = bus.read_byte_data(I2C_IMU_ADDRESS, num)
    # print(a)
    return a

def get_data():
    elapsed_time = t.process_time()

    accel_x = get_decimal(0x2E, 0x2D)
    accel_y = get_decimal(0x30, 0x2F)
    accel_z = get_decimal(0x32, 0x31)

    gyro_x = get_decimal(0x34, 0x33)
    gyro_y = get_decimal(0x36, 0x35)
    gyro_z = get_decimal(0x38, 0x37)

    # all magnetometer data returns 0 because it is not being read correctly
    mag_x = get_decimal(0x11, 0x12)
    mag_y = get_decimal(0x13, 0x14)
    mag_z = get_decimal(0x15, 0x16)

    return np.array([accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z, mag_x, mag_y, mag_z])

def main():
    success = False
    while not success:
        try:
            bus.write_byte_data(I2C_IMU_ADDRESS, 0x06, 0x01) # wake up imu from sleep, try until works
            bus.write_byte_data(I2C_IMU_ADDRESS, 0x31, 0x02) # wake magnetometer from sleep, try until works
            success = True
        except:
            pass

    while(True):
        try:
            data = get_data()
        except:
            print("Connection Lost")
            t.sleep(10)
 
        print("Accel: ", data[0], ",", data[1], ",", data[2])
        print("Gyro: ", data[3], ",", data[4], ",", data[5])
        print("Mag: ", data[6], ",", data[7], ",", data[8])
        print()

        acc = np.array([data[0], data[1], data[2]])
        gyr = np.array([data[3], data[4], data[5]])
        mag = np.array([data[6], data[7], data[8]])
        gyr_rad = gyr * (np.pi/180)
    
        filter.update(gyr_rad,acc,mag)
        # aboves update method can be run instead of update_imu if the magnetometer problem is fixed 
        # filter.update_imu(gyr_rad,acc) #updates the filter and returns roll, pitch, and yaw in quaternion form
        ahrs = filter.quaternion.to_euler_angles()

        # values are between -pi and pi
        curRoll = ahrs[0]
        curPitch = ahrs[1]
        curYaw = ahrs[2]
        
        # print("Roll: ", curRoll, " Pitch: ", curPitch, " Yaw: ", curYaw)
        print()

if(__name__ == '__main__'):
    main()