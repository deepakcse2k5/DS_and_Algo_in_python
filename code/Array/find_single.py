arr = [1, 1, 2, 2, 3, 4, 4, 5, 5]


def find_single(arr):
    val = 2 * (sum(set(arr))) - sum(arr)
    return arr.index(val)


print(find_single(arr))
