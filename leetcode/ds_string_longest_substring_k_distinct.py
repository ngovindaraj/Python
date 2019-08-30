# @file  Longest Substring with At Most K Distinct Characters
# @brief Given a string, find the length of the longest substring T that contains at most k distinct characters.

# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''

# Approach: Two pointer
# time complexity : O(n log n) where n is length of T
# Space complexity : O(n)
def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    cntr = collections.Counter()
    b, e, maxlen = 0, 0, 0
    for e in range(len(s)):
        cntr[s[e]] += 1
        while len(cntr) > k:
            cntr[s[b]] -= 1
            if cntr[s[b]] == 0:
                del cntr[s[b]]
            b += 1
            maxlen = max(maxlen, e-b+1)
        return maxlen
