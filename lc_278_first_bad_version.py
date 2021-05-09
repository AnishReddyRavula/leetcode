"""
leetcode probelm - 278 - First Bad Version
https://leetcode.com/problems/first-bad-version/
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return 1
class Solution(object):
    def __init__(self):
        self.isBadVersion =  isBadVersion

    def firstBadVersion(self, n):
        """
        Use Binary search to find the first bad version
        when the start and end are too close - by one element
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        while start <= end:
            middle = int((start + end) / 2)
            bad_ver = self.isBadVersion(middle)
            if abs(start - end)  < 2:
                return middle + 1
            if bad_ver:
                end = middle
            else:
                start = middle
        return middle