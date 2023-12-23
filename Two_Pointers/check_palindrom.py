nums = [3,7,1,2,8,4,5]
target = 20


def three_sum_values(nums, target):
    if len(nums)<3:
        return False
    else:
        nums.sort()
        for i in range(len(nums)-2):
            j = i
            k = len(nums)-1







