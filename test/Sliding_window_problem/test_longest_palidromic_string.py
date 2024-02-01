import unittest
import sys
sys.path.append('/Users/deemish2/git/DS_and_Algo_in_python/code/Sliding_window_problem')
from longest_palidromic_string import LongestPalindromicSubstring

class TestLongestPalindromicSubstring(unittest.TestCase):

    def setUp(self):
        self.palindrome_calculator = LongestPalindromicSubstring("")

    def test_longest_palindromic_string(self):
        # Test case 1
        self.palindrome_calculator.str1 = "babad"
        result1 = self.palindrome_calculator.longest_palindromic_string()
        self.assertIn(result1, ["bab", "aba"])

        # Add more test cases as needed

    def test_longest_palindromic_string_with_empty_string(self):
        # Test case with an empty string
        self.palindrome_calculator.str1 = ""
        result = self.palindrome_calculator.longest_palindromic_string()
        self.assertEqual(result, "")

    def test_longest_palindromic_string_with_single_character(self):
        # Test case with a single character string
        self.palindrome_calculator.str1 = "a"
        result = self.palindrome_calculator.longest_palindromic_string()
        self.assertEqual(result, "a")

    def test_longest_palindromic_string_with_all_characters_same(self):
        # Test case with all characters being the same
        self.palindrome_calculator.str1 = "ccc"
        result = self.palindrome_calculator.longest_palindromic_string()
        self.assertEqual(result, "ccc")

if __name__ == '__main__':
    unittest.main()
