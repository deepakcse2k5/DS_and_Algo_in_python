nums = [3, 3]
target = 6


def twoSum(nums, target):
    result = {}
    for index, val in enumerate(nums):
        compliment = target - val
        if compliment in result:
            return [result[compliment], index]
        else:
            result[compliment] = index


print(twoSum(nums, target))
