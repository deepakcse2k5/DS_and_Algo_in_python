# merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
# one [1,5].

# Time complexity - O(N * logN)
# Space Complexity - O(N)

class Interval:
    def __init__(self ,start,end) :
        self.start = start
        self.end = end
        
    def print_interval(self):
        print("["+str(self.start)+ ", "+ str(self.end) + "]", end = "")
        
        
def merge(intervals):
    if len(intervals)<2:
        return intervals
    
    # sort the interval from start time
    
    intervals.sort(key=lambda x:x.start)
    
    mergeintervals =[]
    
    start = intervals[0].start
    end = intervals[0].end
    
    for i in range(1,len(intervals)):
        interval = intervals[i]
        if interval.start <= end :
            end = max(interval.end,end)
        else:
            mergeintervals.append(Interval(start,end))
            start = interval.start
            end = interval.end
            
    # add the last interval
    mergeintervals.append(Interval(start,end))
    return mergeintervals


def main():
    print("merged Interval = ",end = "")
    for i in merge([Interval(1,4),Interval(2,5),Interval(7,9)]):
        i.print_interval()
    print()
        
        
main()