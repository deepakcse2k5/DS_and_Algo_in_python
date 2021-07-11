# Minimum Window Sort
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# Time complexity - O(N) and Space Complexity-O(1)

import math

arr = [1, 2, 5, 3, 7, 10, 9, 12]

def shortest_window_sort(arr):
    low , high = 0,len(arr)-1
    
    while (low<high and arr[low]<=arr[low+1]):
        low+=1
    if low==high:
        return 0 # array is already sorted
    
    while (high>0 and arr[high]>=arr[high-1]):
        high-=1
    # fine the minimum and maximum of the subarray
    subarray_max = -math.inf
    subarray_min = math.inf
    for k in range(low,high+1):
        subarray_max = max(subarray_max,arr[k])
        subarray_min = min(subarray_min,arr[k])
        print("max",subarray_max)
        print("min",subarray_min)
    # extend the subarray to include any number which is bigger than the minimum of the subarray   
    while (low>0 and arr[low-1]>subarray_min):
        print("low",low)
        low-=1
        
    # extend the subarray to include any number which is smaller than the maximum of the subarray
    while(high<len(arr)-1 and arr[high+1]<subarray_max):
        high+=1
        
    return high-low+1


print(shortest_window_sort(arr))
    