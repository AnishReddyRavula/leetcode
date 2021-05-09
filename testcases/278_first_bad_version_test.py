import sys

sys.path.append('../')

from lc_278_first_bad_version import Solution

import unittest
from unittest import mock



def bad_version(*args, **kargs):
    if args[0] >= 1:
        return True
    return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        bad_ver_mock = mock.Mock()
        self.solution.isBadVersion = bad_version

    def test_cases(self):
        self.assertEqual(self.solution.firstBadVersion(5), 1)


if __name__ == '__main__':
    unittest.main()