from typing import List

calories = [6, 5, 0, 0]
k = 2
lower = 1
upper = 5


def dietPerformance(calories, k, lower, upper):
    point = 0
    # base case
    if len(calories) < 0:
        return 0
    for start in range(len(calories) - 1):
        for end in range(start + 1, len(calories)):
            if calories[start] + calories[end] < lower:
                point -= 1
            elif calories[start] + calories[end] > upper:
                point += 1
        return point


print(dietPerformance(calories, 2, 1, 5))


def dietPlanPerformance( calories: List[int], k: int, lower: int, upper: int) -> int:
    n = len(calories)
    # base case
    if n < k:
        return 0

    temp = []
    cur = sum(calories[0:k - 1])
    for i in range(0, n - k + 1):
        cur += calories[i + k - 1]
        temp.append(cur)
        cur -= calories[i]

    point = 0
    for j in temp:
        if j > upper:
            point += 1
        elif j < lower:
            point -= 1
    return point


print(dietPlanPerformance([6,5,0,0], 2, 1, 5))
