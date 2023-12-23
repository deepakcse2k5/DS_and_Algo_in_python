# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]

# Time complexity = O(N) + O(N-1) =  O(N) and Space complexity -O(1)

nums = [1, 5, 6, 4, 3, 2]


def cyclic_sorts(nums):
    i=0
    while i <len(nums):
        j = nums[i] -1
        if nums[i]!=nums[j]:
            nums[i] , nums[j] = nums[j] , nums[i]
            
        else:
            i+=1
            
    return nums


print(cyclic_sorts(nums))

            
        
        