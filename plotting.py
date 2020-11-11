import matplotlib.pyplot as plt
import csv

raw_acc_x = []
raw_acc_z = []
raw_roll = []
raw_pitch = []
raw_yaw = []
raw_bearing = []

filt_acc_x = []
filt_acc_z = []
filt_roll = []
filt_pitch = []
filt_yaw = []
filt_bearing = []

raw_length = 0
filtered_length = 0

raw_path = 'imu_out.csv'
filt_path = 'imu_out_filtered.csv'

isFirstRow = True
with open(raw_path,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if(isFirstRow):
            isFirstRow=False
        else:
            raw_length +=1
            raw_acc_x.append(float(row[0]))
            raw_acc_z.append(float(row[2]))
            raw_bearing.append(float(row[3]))
            raw_pitch.append(float(row[10]))
            raw_roll.append(float(row[11]))
            raw_yaw.append(float(row[12]))
            
isFirstRow = True
with open(filt_path,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if(isFirstRow):
            isFirstRow=False
        else:
            filtered_length +=1
            #filt_acc_x.append(float(row[0]))
            filt_acc_z.append(float(row[0]))
            #filt_roll.append(float(row[1]))
            #filt_pitch.append(float(row[2]))
            #filt_yaw.append(float(row[3]))
            #filt_bearing.append(float(row[4]))

raw_time = range(0,raw_length)
filtered_time = range(0,filtered_length)
print('' + str(filtered_length)) # filtered length is not the right value when we plot the results of test_3d_filter

fig1 = plt.figure() #Accel x
plt.title('Accel x')
plt.ylabel("g")
plt.plot(raw_time, raw_acc_x, label="raw accel x")
#plt.plot(filtered_time, filt_acc_x, label="filtered accel x")
plt.legend(loc = "upper left")

figz = plt.figure() #Accel z
plt.title('Accel z')
plt.ylabel("g")
plt.plot(raw_time, raw_acc_z, label="raw accel z")
plt.plot(filtered_time, filt_acc_z, label="filtered accel z")
plt.legend(loc = "upper left")

fig2 = plt.figure() #Roll
plt.title('Roll')
plt.ylabel('Radians')
plt.plot(raw_time, raw_roll, label="raw roll")
#plt.plot(filtered_time, filt_roll, label="filtered roll")
plt.legend(loc = "upper left")

fig3 = plt.figure() #Pitch
plt.title('Pitch')
plt.ylabel('Radians')
plt.plot(raw_time, raw_pitch, label = "raw pitch")
#plt.plot(filtered_time, filt_pitch, label = "filtered pitch")
plt.legend(loc = "upper left")

fig4 = plt.figure() #Yaw
plt.title('Yaw')
plt.ylabel('Radians')
plt.plot(raw_time, raw_yaw, label = "raw yaw")
#plt.plot(filtered_time, filt_yaw, label = "filtered yaw")
plt.legend(loc = "upper left")

fig5 = plt.figure() #Bearing
plt.title('Bearing')
plt.ylabel('Degrees')
plt.plot(raw_time, raw_bearing, label = "raw bearing")
#plt.plot(filtered_time, filt_bearing, label = "filtered bearing")
plt.legend(loc = "upper left")


plt.show()
