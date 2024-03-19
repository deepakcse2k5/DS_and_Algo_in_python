nums = [1, 2, 4, 6, 8, 21]


def find_sum_of_three(nums, target):
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return False


def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-" * 100)


if __name__ == '__main__':
    main()

# Time complexity
# In the solution above, sorting the array takes O(nlog(n)) and
# the nested loop takes O(n**2)to find the triplet.
# Here, n is the number of elements in the input array.
# Therefore, the total time complexity of this solution is O(nlog(n)+n**2), which simplifies to O(n**2).

# Space complexity
# The space complexity of this solution can range from O(log(n)) to
# O(n), as per the sorting algorithm we use. We use the built-in Python function,
# sort(), so the space complexity of the provided solution is O(n).
