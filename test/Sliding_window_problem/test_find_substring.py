import unittest
import sys
sys.path.append('/Users/deemish2/git/DS_and_Algo_in_python/code/Sliding_window_problem')
from find_substring import SmallestSubstring

class TestSmallestSubstring(unittest.TestCase):

    def setUp(self):
        self.substring_finder = SmallestSubstring("", "")

    def test_find_smallest_substring(self):
        # Test case 1
        self.substring_finder.str1 = "abdbca"
        self.substring_finder.pattern = "abc"
        result1 = self.substring_finder.find_smallest_substring()
        self.assertNotEqual(result1, "bca")

        # Add more test cases as needed

    def test_find_smallest_substring_with_empty_string(self):
        # Test case with an empty string
        self.substring_finder.str1 = ""
        self.substring_finder.pattern = "abc"
        result = self.substring_finder.find_smallest_substring()
        self.assertEqual(result, "")

    def test_find_smallest_substring_with_empty_pattern(self):
        # Test case with an empty pattern
        self.substring_finder.str1 = "abdbca"
        self.substring_finder.pattern = ""
        result = self.substring_finder.find_smallest_substring()
        self.assertEqual(result, "")

    def test_find_smallest_substring_with_no_match(self):
        # Test case with no match
        self.substring_finder.str1 = "xyz"
        self.substring_finder.pattern = "abc"
        result = self.substring_finder.find_smallest_substring()
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()
