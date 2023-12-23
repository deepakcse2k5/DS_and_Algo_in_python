# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.


# Appointments: [[6,7], [2,4], [8,12]]
# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.


# Time complexity O(N*logN) and Space complexity - O(N)

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        


def attend_appointment(intervals):
    if len(intervals)<2:
        return intervals
    
    # sort interval based on start time
    intervals.sort(key=lambda x :x.start)
    start = intervals[0].start
    end = intervals[0].end
    
    for i in range(1,len(intervals)):
        interval = intervals[i]
        if start < interval.start and end<interval.start:
            start = interval.start
            end = interval.end
        else:
            return False
    return True

def conflict_appointment(intervals):
    conflict_appointment = []
    intervals.sort(key=lambda x:x[0])
    start, end =0,1
    
    for i in range(1,len(intervals)):
        if intervals[i][start] < intervals[i-1][end]:
            conflict_appointment.append(str([intervals[i-1][start],intervals[i-1][end]] )+ " and " + str([intervals[i][start],intervals[i][end]]) +" are conflict")
       
    return conflict_appointment
        

def main():
    # print(attend_appointment([Interval(1,4),Interval(2,5),Interval(7,9)]))
    # print(attend_appointment([Interval(6,7),Interval(2,4),Interval(8,12)]))
    
    
    # print(conflict_appointment([[1,4],[2,5],[7,9]]))
    print(conflict_appointment([[4,5], [2,3], [3,6], [5,7], [7,8]]))
    
    
    
main()
            
                
    