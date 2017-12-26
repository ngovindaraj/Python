# @file  Palindrome Permutation
# @brief Given a string, determine if a permutation of the string could form a palindrome.

# https://leetcode.com/problems/palindrome-permutation/

'''
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''

# Approach 1: using Set
# time: O(len of string)
# space: time: O(len of string) = O(26)--max possible unique values = O(1)

def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chset = set()
        for ch in s:
            if ch in chset: chset.remove(ch)
            else:           chset.add(ch)
        if len(chset) > 1:
            return False
        return True
