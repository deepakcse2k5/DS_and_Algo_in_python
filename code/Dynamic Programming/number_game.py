# Maximize Score After N Operations

# Input: nums = [3,4,6,8]
# Output: 11
# Explanation: The optimal choice of operations is:
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

# TC :- O(n*2^n * n^2) = O(n^3*2^n)
# SC :- O(n^2*2^n)

nums = [3, 4, 6, 8]

from functools import lru_cache


def max_score(nums):
    n = len(nums)

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @lru_cache(None)
    def dp(step, mask):
        if mask == (1 << n - 1):
            return 0
        ans = 0
        for i in range(n):
            if mask & (1 << i) == 0:
                for j in range(i + 1, n):
                    if mask & (1 << j) == 0:
                        ans = max(ans, step * gcd(nums[i], nums[j]) + dp(step + 1, mask | (1 << i) | (1 << j)))
        return ans

    return dp(1, 0)


print("max score after N operation", max_score(nums))
