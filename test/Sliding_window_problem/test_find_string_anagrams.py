import unittest
import sys
sys.path.append('/Users/deemish2/git/DS_and_Algo_in_python/code/Sliding_window_problem')
from find_string_anagrams import AnagramFinder

class TestAnagramFinder(unittest.TestCase):
    def setUp(self):
        self.finder = AnagramFinder("", "")
    
    def test_find_string_anagrams(self):
        # Test case 1
        self.finder.str1 = "abbcabc"
        self.finder.pattern = "abc"
        result1 = self.finder.find_string_anagrams()
        self.assertEqual(result1, [2, 3, 4])
        
        # Test case 2
        self.finder.str1 = "ppqp"
        self.finder.pattern = "pq"
        result2 = self.finder.find_string_anagrams()
        self.assertEqual(result2, [1, 2])

        # Test case 3
        self.finder.str1 = "abbcabc"
        self.finder.pattern = "abc"
        result3 = self.finder.find_string_anagrams()
        self.assertEqual(result3, [2, 3, 4])

        