import sys

sys.path.append('../')

from lc_35_search_insert_position import Solution

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cases(self):
        self.assertEqual(self.solution.searchInsert([1,2,3,4,5], 4), 3)
        self.assertEqual(self.solution.searchInsert([1,2,3,4,5], 0), 0)
        self.assertEqual(self.solution.searchInsert([1,2,3,4,5], 0), 0)
        self.assertEqual(self.solution.searchInsert([1,2,3,4,5], 6), 5)
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 2), 1)


if __name__ == '__main__':
    unittest.main()