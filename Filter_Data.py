TOTAL_TIME_S = 30
END_NULL_TIME_S = 5
DURATION_TIME_S = 15

def filter(intervals):
    total_time = 0
    

    for time in intervals:
        total_time += time
    
    if total_time < TOTAL_TIME_S:
        print('Total Time is not long enough!')
        return

    for i in range(len(intervals)-1, 0, -1):
        total_time
