import unittest
import sys
sys.path.append('/Users/deemish2/git/DS_and_Algo_in_python/code/Sliding_window_problem')
from find_average_of_subarray import AverageOfSubarrays

class TestAverageOfSubarrays(unittest.TestCase):

    def setUp(self):
        self.arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
        self.avg_calculator = AverageOfSubarrays(self.arr)

    def test_find_avg_of_subarray_brute_force(self):
        # Test case 1
        result1 = self.avg_calculator.find_avg_of_subarray_brute_force(k=5)
        self.assertEqual(result1, [2.2, 2.8, 2.4, 3.6, 2.8])

        # Add more test cases as needed

    def test_find_avg_of_subarray_sliding_window(self):
        # Test case 1
        result1 = self.avg_calculator.find_avg_of_subarray_sliding_window(k=5)
        self.assertEqual(result1, [2.2, 2.8, 2.4, 3.6, 2.8])

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
