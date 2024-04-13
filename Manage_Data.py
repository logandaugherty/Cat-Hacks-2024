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

def calculateBPS(intervals):
    total_time = sum(intervals)
    beats = len(intervals)
    seconds_to_min = 60/DURATION_TIME_S
    BPS = beats/total_time*seconds_to_min
    return BPS

# Test Data
# test_data = []
# for i in range(600):
#     test_data.append(0.9)

# filtered_data = filter(test_data)

# BPS = calculateBPS(filtered_data)
# print(BPS)