# @file  Longest Substring Without Repeating Characters
# @brief Given a string, find the length of the longest substring without repeating characters.

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# 2 pointer but using dictionary to calculate beginning
# time complexity: O(log n)
def lengthOfLongestSubstring(self, s):
    b, maxlen, dict = 0, 0, {}
    for e, char in enumerate(s):
    # Only chars within window influence window beginning
        if dict.get(char, -1) >= b:
            b = dict[char] + 1
        else: # Update maxlen on all cases when window is not affected
            maxlen = max(maxlen, e - b + 1)
        dict[char] = e
    return maxlen




# "abcdefbah" = 7
# "abcabcbb"  = 3
