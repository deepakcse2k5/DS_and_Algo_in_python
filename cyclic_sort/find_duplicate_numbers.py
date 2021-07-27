# Input: [1, 4, 4, 3, 3,5]
# Output: 4


nums = [1,4,4,3,3,5]

def find_duplicate_number(nums):
    i = 0
    duplicate_numbers = []
    while i <len(nums):
        j = nums[i] -1
        
        if nums[i]!=nums[j]:
            nums[i],nums[j] = nums[j] ,nums[i]
        else:
            i+=1
            
    for i in range(len(nums)):
        if nums[i]!=i+1:
            duplicate_numbers.append(nums[i])
        
    return duplicate_numbers



print(find_duplicate_number(nums))