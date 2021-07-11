# Subarrays with Product Less than a Target 

# Input: [2, 5, 3, 10], target=30 
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
# sliding window takes O(N)O(N)O(N) but creating subarrays can take up to O(N^2) in the worst case.
# Therefore overall, our algorithm will take O(N^3)
# Ignoring the space required for the output list, the algorithm runs in O(N) space which is used for the temp list.
#So, at most, we need space for O(N^2) output lists. At worst, each subarray can take O(N) space, so overall, our algorithm’s space complexity will be O(N^3).

from collections import deque


arr = [2,5,3,10]

target = 30

def find_subarrays(arr,target):
    left =0
    product =1
    result =[]
    
    for right in range(len(arr)):
        product *= arr[right]
        while product>target and left<len(arr):
            product/=arr[left]
            left+=1
        # since the product of all numbers from left to right is less 
        # then target then all subarray from left to right have a product less that target.
        # To avoid duplicate , we will start with subarray with only arr[right] and then extend it
        
        temp_list = deque()
        for i in range(right, left-1,-1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
            
    return result
    
    
print(find_subarrays(arr,target))