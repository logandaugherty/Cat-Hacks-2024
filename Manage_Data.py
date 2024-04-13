import random

START_NULL_TIME_S = 3
END_NULL_TIME_S = 1
TOTAL_TIME = 20
duration_time = TOTAL_TIME-END_NULL_TIME_S-START_NULL_TIME_S

def get_start_null_time():
    return START_NULL_TIME_S

def get_end_null_time():
    return END_NULL_TIME_S

def get_read_duration_time():
    return duration_time

def get_total_time():
    return TOTAL_TIME

def filter(intervals):
    new_intervals = []

    if sum(intervals) < duration_time:
        print('Total Time is not long enough!\n Total Time: {0:0.2f}'.format(total_time))
        return
 
    total_time = 0

    for time in intervals:
        total_time += time
        if total_time > START_NULL_TIME_S and total_time < (START_NULL_TIME_S + duration_time):
            new_intervals.append(time)
        elif total_time > (START_NULL_TIME_S + duration_time):
            break
    
    return new_intervals

def calculateBPM(intervals):
    total_time = sum(intervals)
    beats = len(intervals)
    BPS = beats/total_time*60
    return round(BPS)

#  Test Data
test_data = []
for i in range(100):
    test_data.append(random.randrange(900, 1100)/1000.0)
# print(test_data)

filtered_data = filter(test_data)
print(sum(filtered_data))
print(filtered_data)

BPS = calculateBPM(filtered_data)
print(BPS)