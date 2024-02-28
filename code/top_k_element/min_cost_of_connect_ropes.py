from heapq import *
nums = [3,4,5,6]

def min_cost_of_connected_ropes(nums):
    minHeap = []
    for i in nums:
        heappush(minHeap, i)

    result , temp = 0, 0
    while len(minHeap)>1:
        temp = heappop(minHeap) + heappop(minHeap)
        result+=temp
        heappush(minHeap,temp)

    return result



def main():

  print("Minimum cost to connect ropes: " +
        str(min_cost_of_connected_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(min_cost_of_connected_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(min_cost_of_connected_ropes([1, 3, 11, 5, 2])))

main()


# Time Complexity - O(N*logN)

# Space Complexity - O(N)


