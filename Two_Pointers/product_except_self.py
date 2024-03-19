arr = [1,5,10]


def product_except_self(arr):
    n = len(arr)
    res = [1] * n
    left_prod, right_prod = 1, 1
    l = 0
    r = n - 1
    while l < n and r > -1:
        res[l] *= left_prod
        res[r] *= right_prod
        left_prod *= arr[l]
        right_prod *= arr[r]
        l += 1
        r -= 1
    return res


def main():
    inputList = [[1, 5, 10], [3, 5, 0, -3, 1], [7, 8, 9, 10, 11], [2, -4, -8, -11, 11],
                 [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5]]

    # For each input, print the input and its maximum depth
    for i in range(len(inputList)):
        print(str(i + 1) + '.\tnums:', inputList[i])
        print('\tres:', product_except_self(inputList[i]))
        print('-' * 100)


if __name__ == '__main__':
    main()

# Time complexity
# The time complexity of this solution is O(n), where n is the length of the input list arr.
# This is because we iterate through the list once, using two pointers to traverse the list from both ends.

# Space complexity
# The space complexity of this solution is O(1),
# since it doesn’t use any additional array for computations but only constant additional space.
