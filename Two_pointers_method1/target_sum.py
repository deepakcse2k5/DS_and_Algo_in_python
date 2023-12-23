# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Time complexity O(N) and Space Complexity O(1)

def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
    start =0
    end = len(arr)-1
    while start<end:
        if arr[start] + arr[end] == target_sum:
            return [start,end]
        elif arr[start] + arr[end]> target_sum:
            end -=1
        else:
            start+=1

    return [-1, -1]

# hash Table approach
# Time complexity O(N) and Space Complexity O(N)
def pair_with_targetsum1(arr, target_sum):
    nums = {}
    
    for i,num in enumerate(arr):
        if target_sum-num in nums:
            return [nums[target_sum-num],i]
        else:
            nums[arr[i]]= i
    return [-1,-1]
      