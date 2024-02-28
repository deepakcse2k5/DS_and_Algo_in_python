nums = [1,5,12,2,11,5]
K = 3

from heapq import *

def find_kth_smallest_number(nums,K):
    result = []
    for i in range(K):
        heappush(result, -nums[i])
    for i in range(K,len(nums)):
        if nums[i]>result[0]:
            heappop(result)
            heappush(result, -nums[i])
    return -result[0]


print(find_kth_smallest_number(nums, K))


