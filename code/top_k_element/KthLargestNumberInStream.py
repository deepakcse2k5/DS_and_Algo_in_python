from heapq import *


class KthLargestNumberInStream:

    minHeap = []
    def __init__(self, nums,K) -> None:
        self.K = K
        for num in nums:
            self.add(num)

    def add(self,num):
        heappush(self.minHeap,num)

        if len(self.minHeap) > self.K:
            heappop(self.minHeap)
        return self.minHeap[0]
    

def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()


# Time complexity - O(logK) because we are inserting new number in Heap
# Space Complexity - O(K) for storing numbers in Heap


    