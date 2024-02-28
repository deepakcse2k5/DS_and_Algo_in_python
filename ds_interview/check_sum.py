nums = [3,1,4,2,6,9,8]
target = 11

def check_sum(nums, target):
    if len(nums)==0:
        return
    d  = []
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [d.index(target-nums[i]),i]
        else:
            d.append(nums[i])

    return []

def main():
    print(check_sum(nums, target))


main()