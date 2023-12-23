class LongestContiguousSubarray:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k

    def length_of_longest_substring(self):
        start = 0
        max_length = 0
        num_frequency = {}
        max_repeated_count = 0

        for end in range(len(self.arr)):
            right_num = self.arr[end]

            if right_num not in num_frequency:
                num_frequency[right_num] = 0
            num_frequency[right_num] += 1
            max_repeated_count = max(max_repeated_count, num_frequency[right_num])

            if (end - start + 1 - max_repeated_count) > self.k:
                left_num = self.arr[start]
                num_frequency[left_num] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length

if __name__ == '__main__':
    arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3

    subarray_calculator = LongestContiguousSubarray(arr, k)
    result = subarray_calculator.length_of_longest_substring()
    print(result)
