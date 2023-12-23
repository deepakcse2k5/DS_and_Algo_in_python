import unittest
import sys
sys.path.append('/Users/deemish2/git/DS_and_Algo_in_python/code/Sliding_window_problem')
from length_of_longest_substring import LongestRepeatingSubstring

class TestLongestRepeatingSubstring(unittest.TestCase):

    def setUp(self):
        self.substring_calculator = LongestRepeatingSubstring("", 0)

    def test_length_of_longest_substring(self):
        # Test case 1
        self.substring_calculator.str1 = "aabccbb"
        self.substring_calculator.k = 2
        result1 = self.substring_calculator.length_of_longest_substring()
        self.assertEqual(result1, 5)

        # Add more test cases as needed

    def test_length_of_longest_substring_with_empty_string(self):
        # Test case with an empty string
        self.substring_calculator.str1 = ""
        self.substring_calculator.k = 2
        result = self.substring_calculator.length_of_longest_substring()
        self.assertEqual(result, 0)

    def test_length_of_longest_substring_with_zero_k(self):
        # Test case with k = 0
        self.substring_calculator.str1 = "aabccbb"
        self.substring_calculator.k = 1
        result = self.substring_calculator.length_of_longest_substring()
        self.assertEqual(result, 1)

    def test_length_of_longest_substring_with_negative_k(self):
        # Test case with negative k
        self.substring_calculator.str1 = "aabccbb"
        self.substring_calculator.k = -1
        result = self.substring_calculator.length_of_longest_substring()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
