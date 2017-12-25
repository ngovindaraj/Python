# @file Is Subsequence
# @brief Given a string s and a string t, check if s is subsequence of t.

# https://leetcode.com/problems/is-subsequence

'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

'''

# Approach 1: 2 pointer
# time complexity: O(length of s + length of t)
# space complexity: O(1)

def isSubsequence(self, s_string, t_string):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = 0
        for s in s_string:
            idx = t_string.find(s, idx)  # Find first occurence of each char in s in t_string[idx:]
            if idx == -1: return False
            else:         idx += 1
        return True
        
        
 
    
    
    