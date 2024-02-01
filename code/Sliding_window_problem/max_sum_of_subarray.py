class MaxSumSubarray:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k

    def max_sum_of_subarray(self):
        curr_max = 0
        global_max = 0
        start = 0

        for i in range(len(self.arr)):
            curr_max += self.arr[i]
            if i >= self.k - 1:
                global_max = max(curr_max, global_max)
                curr_max -= self.arr[start]
                start += 1

        return global_max


if __name__ == '__main__':
    arr = [2, 1, 5, 1, 3, 2]
    k = 3

    max_sum_calculator = MaxSumSubarray(arr, k)
    result = max_sum_calculator.max_sum_of_subarray()
    print(result)
