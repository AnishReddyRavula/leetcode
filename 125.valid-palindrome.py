# leetcode problem - 125
# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, payload):
        f_char_i = 0
        l_char_i = len(payload) - 1

        # loop until the first char of the payload and last char of the payload are same
        while f_char_i < l_char_i:
            if not payload[f_char_i].isalnum():
                f_char_i += 1
            elif not payload[l_char_i].isalnum():
                l_char_i -= 1
            elif payload[f_char_i].lower() != payload[l_char_i].lower():
                return False
            else:
                f_char_i += 1
                l_char_i -= 1
        return True