import unittest
import sys
sys.path.append('/Users/deemish2/git/DS_and_Algo_in_python/code/Sliding_window_problem')
from length_of_longest_substring_with_replacement import LongestContiguousSubarray

class TestLongestContiguousSubarray(unittest.TestCase):

    def setUp(self):
        self.subarray_calculator = LongestContiguousSubarray([], 0)

    def test_length_of_longest_substring(self):
        # Test case 1
        self.subarray_calculator.arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
        self.subarray_calculator.k = 3
        result1 = self.subarray_calculator.length_of_longest_substring()
        self.assertEqual(result1, 9)

        # Add more test cases as needed
        self.subarray_calculator.arr = [0, 1, 0, 0, 1, 1, 0, 1, 1]
        self.subarray_calculator.k = 2
        result2 = self.subarray_calculator.length_of_longest_substring()
        self.assertEqual(result2, 6)

    def test_length_of_longest_substring_with_empty_array(self):
        # Test case with an empty array
        self.subarray_calculator.arr = []
        self.subarray_calculator.k = 3
        result = self.subarray_calculator.length_of_longest_substring()
        self.assertEqual(result, 0)

    def test_length_of_longest_substring_with_zero_k(self):
        # Test case with k = 0
        self.subarray_calculator.arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
        self.subarray_calculator.k = 0
        result = self.subarray_calculator.length_of_longest_substring()
        self.assertEqual(result, 2)

    def test_length_of_longest_substring_with_negative_k(self):
        # Test case with negative k
        self.subarray_calculator.arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
        self.subarray_calculator.k = -1
        result = self.subarray_calculator.length_of_longest_substring()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
