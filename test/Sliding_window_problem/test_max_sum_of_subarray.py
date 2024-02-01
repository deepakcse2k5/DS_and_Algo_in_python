import unittest
import sys
sys.path.append('/Users/deemish2/git/DS_and_Algo_in_python/code/Sliding_window_problem')
from max_sum_of_subarray import MaxSumSubarray

class TestMaxSumSubarray(unittest.TestCase):

    def setUp(self):
        self.max_sum_calculator = MaxSumSubarray([], 0)

    def test_max_sum_of_subarray(self):
        # Test case 1
        self.max_sum_calculator.arr = [2, 1, 5, 1, 3, 2]
        self.max_sum_calculator.k = 3
        result1 = self.max_sum_calculator.max_sum_of_subarray()
        self.assertEqual(result1, 9)

        # Add more test cases as needed

    def test_max_sum_of_subarray_with_empty_array(self):
        # Test case with an empty array
        self.max_sum_calculator.arr = []
        self.max_sum_calculator.k = 3
        result = self.max_sum_calculator.max_sum_of_subarray()
        self.assertEqual(result, 0)

    def test_max_sum_of_subarray_with_k_greater_than_array_length(self):
        # Test case with k greater than array length
        self.max_sum_calculator.arr = [2, 1, 5, 1, 3, 2]
        self.max_sum_calculator.k = 10
        result = self.max_sum_calculator.max_sum_of_subarray()
        self.assertEqual(result, 0)

    def test_max_sum_of_subarray_with_negative_numbers(self):
        # Test case with negative numbers
        self.max_sum_calculator.arr = [-2, -3, 4, -1, -2, 1, 5, -3]
        self.max_sum_calculator.k = 3
        result = self.max_sum_calculator.max_sum_of_subarray()

        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
