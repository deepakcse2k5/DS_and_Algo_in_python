# House Robber
#
# You are a robber planning to rob houses along a street. Each house has a certain amount of treasure stashed, the only constraint stopping you from robbing every one of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

from typing import List


def house_rob(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) < 2:
        return max(nums)

    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1] , nums[i] + dp[i - 2])
    return dp[-1]


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = house_rob(nums)
    print(res)
