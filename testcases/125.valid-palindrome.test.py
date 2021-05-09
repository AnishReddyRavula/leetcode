import sys

sys.append('../')

from 125_valid_palindrome import Solution

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cases(self):
        pass


if __name__ == '__main__':
    unittest.main()