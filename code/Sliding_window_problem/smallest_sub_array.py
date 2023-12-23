# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
# Time Complexity O(N)

import math

arr = [2, 1, 5, 2, 3, 2]
s = 7

def smallest_subarray(arr,s):
    sum =0
    start = 0
    min_length =math.inf
    
    for end in range(0,len(arr)):
        sum += arr[end]
        print("sum:",sum)
        
        while sum >= s:
            min_length = min(min_length,end-start+1)
            sum -= arr[start]
            start += 1
    if min_length == math.inf:
        return 0
    return min_length

print(smallest_subarray(arr,s))
            
            