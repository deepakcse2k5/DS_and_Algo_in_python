class AverageOfSubarrays:
    def __init__(self, arr):
        self.arr = arr

    def find_avg_of_subarray_brute_force(self, k):
        if len(self.arr) < k:
            return []
        avg_arr = []
        for i in range(len(self.arr) - k + 1):
            avg_arr.append(sum(self.arr[i:i+k]) / k)
        return avg_arr

    def find_avg_of_subarray_sliding_window(self, k):
        if len(self.arr) < k:
            return []
        result = []
        start = 0
        sum = 0.0
        for i in range(len(self.arr)):
            sum += self.arr[i]
            if i >= k - 1:
                result.append(sum / k)
                sum -= self.arr[start]
                start += 1
        return result


if __name__ == '__main__':
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    avg_calculator = AverageOfSubarrays(arr)

    # Test the brute-force approach
    result_brute_force = avg_calculator.find_avg_of_subarray_brute_force(k=5)
    print(result_brute_force)

    # Test the sliding window approach
    result_sliding_window = avg_calculator.find_avg_of_subarray_sliding_window(k=5)
    print(result_sliding_window)
