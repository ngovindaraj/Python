# @file  Find All Anagrams in a String
# @brief Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# https://leetcode.com/problems/find-all-anagrams-in-a-string/

'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

# 2-pointer approach: moving window
# time complexity: O(length of s + length of p)
# space: O(length of p)

def findAnagrams(self, s, p):
    lst = []
    pDict = collections.Counter(p)
    sDict = collections.Counter(s[0:len(p)-1])   # stop counter one element less than one p-chunk
    sLen, pLen = len(s), len(p)
    for i in range(0, sLen - pLen + 1):         # len = e-b+1; plen = e-b+1; b = e-plen+1; b =slen-1-plen+1; b = slen-plen
        oldChar, newChar = s[i], s[i + pLen - 1]
        sDict[newChar] += 1                     # add e
        if sDict == pDict:  lst.append(i)       # check dict
        sDict[oldChar] -= 1                     # remove b
        if sDict[oldChar] == 0: del sDict[oldChar]
    return lst
