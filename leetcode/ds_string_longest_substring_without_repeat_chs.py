# @file  Longest Substring Without Repeating Characters
# @brief Given a string, find the length of the longest substring without repeating characters.


# https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

# Approach: two pointer
# time complexity : O(n)
# Space complexity : O(n) where every element in the list is unique
def lengthOfLongestSubstring(self, s: str) -> int:
    b, maxlen = 0, 0
    cset = set()
    for e in range(len(s)):
        while s[e] in cset:
            cset.remove(s[b])
            b += 1
        cset.add(s[e])
        maxlen = max(maxlen, e-b+1)
    return maxlen
