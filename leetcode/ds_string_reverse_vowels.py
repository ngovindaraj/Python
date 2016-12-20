# @file  Reverse Vowels
# @brief Reverse only vowels in a string

# https://leetcode.com/problems/reverse-vowels-of-a-string/

'''
Write a function that takes a string as input and reverse 
only the vowels of a string.
Example 1: Given s = "hello", return "holle".
Example 2: Given s = "leetcode", return "leotcede".
Note: The vowels does not include the letter "y".
'''

Approach 1: Two pointer approach
def reverseVowels(self, s):
  vowset = {'a','e','i','o','u','A','E','I','O','U'}
  lst  = list(s)
  b, e = 0, len(lst) - 1  #use property: len = e - b + 1 
  while b < e:
    if    lst[b] not in vowset: b += 1
    elif  lst[e] not in vowset: e -= 1
    else:
      lst[b], lst[e] = lst[e], lst[b] #tupple assignments
      b, e = b + 1, e - 1
  return ''.join(lst)

# "hello", "holle"
# "aA",    "Aa"
# "",      ""
