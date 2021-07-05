# Find our the maximum sum of subarray
# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Time complexity - O(N)

arr = [2,1,5,1,3,2]
k=3
def max_sum_of_subarray(arr,k):
    curr_max = 0
    global_max = 0
    start =0

    
    for i in range(len(arr)):
        curr_max+=arr[i]
        if i>=k-1:
            global_max = max(curr_max,global_max)
            curr_max-=arr[start]
            start+=1
    return global_max

print(max_sum_of_subarray(arr,k))
            
        
    