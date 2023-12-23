# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.


# Time complexity- O(N) and Space complexity -O(1)

nums = [2,3,1,8,2,3,5,1]


def find_missing_numbers(nums):
    missing_numbers=[]
    i =0
    while i < len(nums):
        j = nums[i]-1
        if nums[i] !=nums[j] :
            nums[i],nums[j] = nums[j] , nums[i]
        else:
             i+=1
             
    for i in range(len(nums)):
        if nums[i] !=i+1:
            missing_numbers.append(i+1)
        
        
    return missing_numbers


print(find_missing_numbers(nums))