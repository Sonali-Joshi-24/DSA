'''
Meeting Rooms
given an array of meeting time intervals consisting of start and end times
[[s1,e1], [s2,e2], ...] (si < ei) determine if a person can attend all meetings

Note: (0,8) , (8, 10) --> is not a conflict

Example:
input : intervals : [(0,30), (5, 10), (15,20)]
output : false
Explanation: (0,30), (5,10) and (0,30),(15,20) will conflict

sort the input based on the start time and do a linear traversal 
time : O(NlogN) , space:O(1)
'''

def meetingRooms(intervals):
    intervals.sort(key = lambda i : i.start)

    for i in range(1,len(intervals)):
        i1 = intervals[i-1]
        i2 = intervals[i]

        if i1.end > i2.end:
            return False
    return True

intervals = [(0,30), (5, 10), (15,20)]
print(meetingRooms(intervals))