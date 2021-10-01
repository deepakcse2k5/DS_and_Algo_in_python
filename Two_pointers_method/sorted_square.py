from typing import List
import collections


def sortedSquares( nums: List[int]) -> List[int]:
    result = collections.deque()
    l, r= 0, len(nums) - 1

    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])
        if left > right:
            result.appendleft(left * left)
            l += 1

        else:
            result.appendleft(right * right)
            r -= 1
    return list(result)


print(sortedSquares([-4, -1, 0, 3, 10]))
