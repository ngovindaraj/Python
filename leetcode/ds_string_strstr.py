# @file  Strstr
# @brief Find first occurence of needle in a haystack

# https://leetcode.com/problems/implement-strstr/

'''
Implement strStr().
Returns the index of the first occurrence of needle in
haystack, or -1 if needle is not part of haystack.
'''

#Approach 1: Brute force 2-loop approach
  def strStr(self, haystack, needle):
    for i in range(0, len(haystack) - len(needle) + 1): #stop i early to avoid going beyond index
      if haystack[i : i + len(needle)] == needle : return i
    return -1
        
#Approach 2: Boyer-Moore
#Need to learn and implement

# haystack,  needle,       idx
# "",            "",         0
# "abc",       "bc",         1
# "aaaa",     "aaa",         0

