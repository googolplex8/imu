import csv
from collections import deque


###input params###########
num_measurements = 10     #if rapid change in measurements, num_measurements must be lower
threshold = 0.04          #less than
weight = 0.6              #current data
##########################

raw_path = 'imu_out.csv'
isFirstRow = True
prev_accel = 0
d = deque()
average = 0

def find_average(input):
    sum = 0
    for elem in input:
        sum += elem
    return sum/len(input)
    
def filter(prev_accel, cur_accel):
    if (len(d) < num_measurements):
        d.append(cur_accel)
        average = find_average(d)
    else:
        d.append(cur_accel)
        d.popleft()
        average = find_average(d)
        
    #thresholding to 0
    if (abs(cur_accel-average) < threshold):
        toReturn = average
    #else, perform simple low-pass filtering
    else:
        toReturn = (weight) * cur_accel + (1-weight) * prev_accel

    return toReturn

with open('imu_out_filtered.csv', mode='w') as filter_file:
    print('opened filtered csv')
    with open(raw_path,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if(isFirstRow):
                isFirstRow=False
            else:
                #print ("row[0] is " + row[0])
                prev_accel = filter(prev_accel, float(row[2]))
                writer = csv.writer(filter_file, delimiter=',', lineterminator = '\n')
                #print("filtered accel is " + str(prev_accel))
                writer.writerow([prev_accel])
            
