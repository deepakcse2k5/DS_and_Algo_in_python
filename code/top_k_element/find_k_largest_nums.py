nums = [3,1,5,12,2,11]
k =3 
from heapq import *
def find_k_largest_nums(nums, k):
    result = []
    for i in range(k):
        heappush(result, nums[i])
    
    for i in range(k, len(nums)):
        if nums[i] > result[0]:
            heappop(result)
            heappush(result, nums[i])
    return result


print(find_k_largest_nums(nums, k))


# Time compleity - O(K*logK + (N-K)*logK) which is O(N*logK)

# Space Complexity - O(K)
