# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

arr = [-2,0,1,2]
target_sum =2
import math

def triplet_sum_close_to_target(arr,target_sum):
    arr.sort()
    smallest_diff = math.inf
    for i in range(len(arr)-2):
        left =0
        right = len(arr)-1
        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff ==0:
                return target_sum- target_diff
            
            if abs(target_diff) < abs(smallest_diff) or (abs(target_diff)== abs(smallest_diff)) or target_diff>smallest_diff:
                smallest_diff = target_diff
            if target_diff > 0:
                left+=1
            else:
                right -=1
                
    return target_sum - smallest_diff


            
        
print(triplet_sum_close_to_target(arr,target_sum))