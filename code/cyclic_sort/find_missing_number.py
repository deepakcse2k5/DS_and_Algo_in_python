# Input: [8, 3, 5, 2, 4, 6, 0, 1]
# Output: 7


# Time complexity = O(N) + O(N-1) =  O(N) and Space complexity -O(1)

nums = [8, 3, 5, 2, 4, 6, 0, 1]

def find_missing_number(nums):
    i =0
    while i < len(nums) :
        j = nums[i]
        if  nums[i] < len(nums) and nums[i] != nums[j] :
            nums[i] , nums[j] = nums[j] , nums[i]
        else:
            i+=1
    for i in range(len(nums)):
        if nums[i]!=i:
            break
    return i


print(find_missing_number(nums))
        