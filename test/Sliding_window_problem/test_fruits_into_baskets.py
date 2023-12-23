import unittest
import sys
sys.path.append('/Users/deemish2/git/DS_and_Algo_in_python/code/Sliding_window_problem')

from fruits_into_basket import FruitBasket


class TestFruitBasket(unittest.TestCase):


    def test_max_fruits_in_baskets(self):
        # Test case 1
        fruits1 = ['A', 'B', 'C', 'B', 'B', 'C']
        fruit_basket1 = FruitBasket(fruits1)
        result1 = fruit_basket1.max_fruits_in_baskets()
        self.assertEqual(result1, 5)

        # Test case 2
        fruits2 = ['A', 'B', 'A', 'C', 'B', 'B', 'C']
        fruit_basket2 = FruitBasket(fruits2)
        result2 = fruit_basket2.max_fruits_in_baskets()
        self.assertEqual(result2, 4)

        # Test case 3
        fruits3 = ['A', 'B', 'C', 'A', 'C']
        fruit_basket3 = FruitBasket(fruits3)
        result3 = fruit_basket3.max_fruits_in_baskets()
        self.assertEqual(result3, 3)


if __name__ == '__main__':
    unittest.main()