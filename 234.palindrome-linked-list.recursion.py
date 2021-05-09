# leetcode problem - 234 - Recursive solution
# https://leetcode.com/problems/palindrome-linked-list

class Solution(object):
    # idea is to get the end of the linked list and compare it with
    # the beginnig of the head, if those values match then the next
    # sublist's head and end can be compared
    def _isPalindrome(self, end):
        # return True when end of list is found
        if not end:
            return True
        # recursively call the method with next node
        is_pali = self._isPalindrome(end.next)
        # if its not palindrome stop execution
        if not is_pali:
            return False
        # if the end of the sublist is not equal to the current head
        if self.head.val != end.val:
            return False
        # move the head so that the sublist will have the next head
        # to compare with the end
        self.head = self.head.next
        return True
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.head = head
        return self._isPalindrome(head)

