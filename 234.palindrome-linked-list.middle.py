# leetcode problem - 234 - middle solution
# https://leetcode.com/problems/palindrome-linked-list

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first_half_nodes = []
        slow_head = head
        # finding middle of the LL
        while head:
            first_half_nodes.append(slow_head)
            slow_head = slow_head.next
            if head.next:
                head = head.next.next
            else:
                # while jumping on odd places, it will reach the end where it can't find next
                # such cases ignore the middle digit - Eg: 3rd digit in 5 digit palindrome
                if len(first_half_nodes) > 0:
                    first_half_nodes.pop()
                break
        second_half_head = slow_head
        l = len(first_half_nodes)
        # check from the middle node to the end of Linked list
        # with elements in first_half_nodes if its a palindrome
        for i in range(l, 0, -1):
            if second_half_head.val == first_half_nodes[i - 1].val:
                second_half_head = second_half_head.next
            else:
                return False
        return True