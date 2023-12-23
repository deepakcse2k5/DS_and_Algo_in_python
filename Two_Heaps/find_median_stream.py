import heapq

class MedianofStream:
    def __init__(self):
        # Initialize two heaps - max_heap for the lower half, min_heap for the upper half
        self.max_heap = [] # Max-heap to store the smaller half of the data
        self.min_heap = [] # Min-heap to store the larger half of the data

    def addNum(self,num:int)-> None:
        if not self.max_heap or num<=-self.max_heap[0]:
            heapq.heappush(self.max_heap,-num)
        else:
            heapq.heappush(self.min_heap,num)

        if len(self.max_heap)> len(self.min_heap)+1:
            heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))


    def findMedian(self) -> float:
        if len(self.max_heap)==len(self.min_heap):
            return (-self.max_heap[0]+self.min_heap[0])/2.0
        else:
            return -self.max_heap[0]/1.0

medianFinder = MedianofStream()
medianFinder.addNum(1)
medianFinder.addNum(2)
medianFinder.addNum(3)
medianFinder.addNum(4)
medianFinder.addNum(5)

print(medianFinder.findMedian())  # Output: 3.0



# Time complexity
# The time complexity of the Insert Num method will change depending on how many numbers have already been received from the stream. So, the time complexity is amortized over the number of insert operations.
#
# Each insert operation will trigger a heapify process that runs in O(logn) times, where n is the count of numbers received so far from the stream.
# Because of this, the cumulative complexity of a sequence of n insert operations is described by the expression log1+log2+log3+..+logn.
#
# This expression simplifies to logn!, which, as per Stirling’s approximation, is O(nlogn)
# . As we have performed n insert operations, the amortized time complexity of one insert operation is O(nlogn/n), that is, O(logn).
# The time complexity of the Find Median method will be O(1) since retrieving the top element of a heap is a constant-time operation,
# and we need to do at most two such retrievals.
#
# Space complexity
# The space complexity will be O(1) since no additional space is used other than that which is required to store the numbers received from the data stream.





