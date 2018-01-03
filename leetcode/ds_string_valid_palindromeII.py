# @file  Valid Palindrome II
# @brief Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# https://leetcode.com/problems/valid-palindrome-ii/

'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

# time complexity: O(length of str) = O(n)
# space complexity: O(1)


class Solution:
    # If palindrome, return b > e, else return first mismatch b, e
    def checkPalindrome(self, s, b, e):
        while b <= e and s[b] == s[e]:
            b, e = b + 1, e - 1
        return (b > e), b, e

    def validPalindrome(self, s):
        isPalindrome, b, e = self.checkPalindrome(s, 0, len(s) - 1)
        if not isPalindrome:  # We have a mismatch in check Palindrome
            return (self.checkPalindrome(s, b + 1, e)[0] | self.checkPalindrome(s, b, e - 1)[0])
        else:   # This is a proper palindrome by default
            return True
