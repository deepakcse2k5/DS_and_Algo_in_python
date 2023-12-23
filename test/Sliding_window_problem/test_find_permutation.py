import unittest
import sys
sys.path.append('/Users/deemish2/git/DS_and_Algo_in_python/code/Sliding_window_problem')
from find_string_anagrams import AnagramFinder

class TestAnagramFinder(unittest.TestCase):

    def setUp(self):
        self.anagram_finder = AnagramFinder("", "")

    def test_find_string_anagrams(self):
        # Test case 1
        self.anagram_finder.str1 = "abbcabc"
        self.anagram_finder.pattern = "abc"
        result1 = self.anagram_finder.find_string_anagrams()
        self.assertEqual(result1, [2, 3, 4])

        # Add more test cases as needed

    def test_find_string_anagrams_with_empty_string(self):
        # Test case with empty string and pattern
        self.anagram_finder.str1 = ""
        self.anagram_finder.pattern = ""
        result = self.anagram_finder.find_string_anagrams()
        self.assertEqual(result, [])

    def test_find_string_anagrams_with_empty_pattern(self):
        # Test case with empty pattern
        self.anagram_finder.str1 = "abbcabc"
        self.anagram_finder.pattern = ""
        result = self.anagram_finder.find_string_anagrams()
        self.assertNotEqual(result, [])

    def test_find_string_anagrams_with_no_anagrams(self):
        # Test case with no anagrams
        self.anagram_finder.str1 = "xyz"
        self.anagram_finder.pattern = "abc"
        result = self.anagram_finder.find_string_anagrams()
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
