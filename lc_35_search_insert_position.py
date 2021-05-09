"""
leetcode probelm - 35 - search insert position
https://leetcode.com/problems/search-insert-position/
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        found = False
        while start < end:
            middle = int((start + end) / 2)
            if nums[middle] == target:
                found = True
                break
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle
        # if not able to find the target and
        # if the middle from search is less than the target
        # return the next index where new number can be inserted
        if not found and nums[middle] < target:
            return middle + 1
        return middle
