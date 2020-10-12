import matplotlib.pyplot as plt
import csv

acc_x = []
acc_y = []
acc_z = []
gyr_x = []
gyr_y = []
gyr_z = []
mag_x = []
mag_y = []
mag_z = []

isFirstRow = True
length = 0

with open('test_data.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if(isFirstRow):
            isFirstRow=False
        else:
            #skip first row somehow
            length +=1
            acc_x.append(float(row[0]))
            acc_y.append(float(row[1]))
            acc_z.append(float(row[2]))
            gyr_x.append(float(row[3]))
            gyr_y.append(float(row[4]))
            gyr_z.append(float(row[5]))
            mag_x.append(float(row[6]))
            mag_y.append(float(row[7]))
            mag_z.append(float(row[8]))

time = range(0,length)

fig = plt.figure()
plt.title('IMU Data')

ax1 = fig.add_subplot(311)
ax1.title.set_text('Accelerometer')
ax1.set_ylabel("m/s^2")
line1 = ax1.plot(time, acc_x, label="x")
line2 = ax1.plot(time, acc_y, label="y")
line3 = ax1.plot(time, acc_z, label="z")
ax1.tick_params(axis='x', which='both', bottom='off',top='off',labelbottom='off')
ax1.legend((line1, line2, line3), ("x", "y", "z"))


ax2 = fig.add_subplot(312)
ax2.title.set_text('Gyroscope')
ax2.set_ylabel("rad/s")
ax2.tick_params(axis='x', which='both', bottom='off',top='off',labelbottom='off')
line4 = ax2.plot(time, gyr_x)
line5 = ax2.plot(time, gyr_y)
line6 = ax2.plot(time, gyr_z)
ax2.legend((line4, line5, line6), ("x", "y", "z"))


ax3 = fig.add_subplot(313)
ax3.title.set_text('Magnetometer')
ax3.set_ylabel("uT")
line7 = ax3.plot(time, mag_x)
line8 = ax3.plot(time, mag_y)
line9 = ax3.plot(time, mag_z)
ax3.legend((line7, line8, line9), ("x", "y", "z"))


plt.show()
