# Given a set of intervals, find out if any two intervals overlap.

# Intervals: [[1,4], [2,5], [7,9]]
# Output: true
# Explanation: Intervals [1,4] and [2,5] overlap

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def print_interval(self):
        print("["+str(self.start) + "," + str(self.end) + "]", end ="")
        
def overlap_interval(intervals):
    if len(intervals)<2:
        return intervals
    
    # sort interval based on start time
    intervals.sort(key=lambda x:x.start)
    
    overlap_interval =[]
    
    start = intervals[0].start
    end = intervals[0].end
    
    for i in range(1,len(intervals)):
        interval = intervals[i]
        
        if interval.start <=end:
            overlap_interval.append(Interval(start,end))
            overlap_interval.append(Interval(interval.start,interval.end))
            end = max(interval.end,end)
        else:
            start = interval.start
            end = interval.end
            
    return overlap_interval

def main():
    print("overlap Interval = ",end = "")
    for i in overlap_interval([Interval(1,4),Interval(2,5),Interval(7,9)]):
        i.print_interval()
    print()
        
        
main()
            