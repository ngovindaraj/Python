# @file  Longest Palindrome
# @brief given string, find length of longest possible palindrome

# https://leetcode.com/problems/longest-palindrome

'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.
'''

# Approach 1: dictionary
def longestPalindrome(self, s):
    length = 0
    odd = False
    dict = {}
    for elem in s:
        dict[elem] = dict.get(elem, 0) + 1
    for k, v in dict.items():
        length += (v/2) *2
        odd = odd | (v % 2)
        if odd == True:
            length += 1
        return length

# Approach 2: math based using collections
import collections
def longestPalindrome2(self, s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)
