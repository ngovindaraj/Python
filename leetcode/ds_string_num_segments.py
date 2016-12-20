# @file  Number of Segments
# @brief Count the number of segments (words) in a string

# https://leetcode.com/problems/number-of-segments-in-a-string/

'''
Count the number of segments in a string, where a segment is defined
to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.
Example:
Input: "Hello, my name is John"
Output: 5
'''

def countSegments(self, s):
  lst = s.split()
  return len(lst)

#"Hello, my name is John"  5
#"   ,   "                 1
#" "                       0
#" @ ab, sdfwe !"          4

