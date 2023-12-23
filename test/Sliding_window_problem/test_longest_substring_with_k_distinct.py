import unittest
import sys
sys.path.append('/Users/deemish2/git/DS_and_Algo_in_python/code/Sliding_window_problem')

from longest_substring_with_k_distinct import LongestSubstringWithKDistinct

class TestLongestSubstringWithKDistinct(unittest.TestCase):

    def test_find_longest_substring(self):
        # Test case 1
        str1 = "cbbebi"
        k = 3
        calculator1 = LongestSubstringWithKDistinct(str1, k)
        result1 = calculator1.find_longest_substring()
        self.assertEqual(result1, 5)

        # Test case 2
        str2 = "abcabcbb"
        k = 2
        calculator2 = LongestSubstringWithKDistinct(str2, k)
        result2 = calculator2.find_longest_substring()
        self.assertEqual(result2, 4)

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
