# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

# Meetings: [[1,4], [2,5], [7,9]]
# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
# occur in any of the two rooms later.


class Meeting:
    def __init__(self,start,end):
        self.start= start
        self.end = end
        
def min_meeting_rooms(meetings):
    if len(meetings)<1:
        return -1
    
    meetings.sort(key=lambda x:x.start)
    
    start = meetings[0].start
    end = meetings[0].end
    count =0
    
    for i in range(len(meetings)):
        meeting = meetings[i]
        
        if end >= meeting.start :
            # print("count",count,[meeting.start,meeting.end])
            count +=1
            # end = max(end,meeting.end)
            
        else:
            start = meeting.start
            end = meeting.end
            
    return count

def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))

    
main()