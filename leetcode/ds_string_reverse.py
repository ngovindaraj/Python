# @file  Reverse String
# @brief Reverse an entire string

# https://leetcode.com/problems/reverse-string/

'''
Write a function that takes a string as input and returns the
string reversed.
Example: Given s = "hello", return "olleh".
'''

#Approach 1: Use Array slicing approach
def reverseString(self, s):
  return s[::-1]

#Approach 2: Two pointer approach
def reverseString(self, s):
  lst  = list(s)
  b, e = 0, len(lst) - 1  #use property: len = e - b + 1 
  while b < e:
    lst[b], lst[e] = lst[e], lst[b] #tupple assignments
    b, e = b + 1, e - 1
  return ''.join(lst)
