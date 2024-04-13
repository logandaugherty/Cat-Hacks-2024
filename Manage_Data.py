# import random

TOTAL_TIME_S = 20
END_NULL_TIME_S = 1
DURATION_TIME_S = 15

def filter(intervals):
    new_intervals = []

    if sum(intervals) < TOTAL_TIME_S:
        print('Total Time is not long enough!\n Total Time: {0:0.2f}'.format(total_time))
        return
 
    total_time = 0

    for i in range(len(intervals)-1, 0, -1):
        time = intervals[i]
        total_time += time
        if total_time > END_NULL_TIME_S and total_time < (END_NULL_TIME_S + DURATION_TIME_S):
            new_intervals.append(time)
        elif total_time > (END_NULL_TIME_S + DURATION_TIME_S):
            break
    
    return new_intervals

def calculateBPM(intervals):
    total_time = sum(intervals)
    beats = len(intervals)
    BPS = beats/total_time*60
    return round(BPS)

#  Test Data
# test_data = []
# for i in range(100):
#     test_data.append(random.randrange(900, 1100)/1000.0)
# # print(test_data)

# filtered_data = filter(test_data)
# print(sum(filtered_data))
# print(filtered_data)

# BPS = calculateBPM(filtered_data)
# print(BPS)