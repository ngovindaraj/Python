
# @file  Word Pattern
# @brief Given 2 sets check if it is a bijection

# https://leetcode.com/problems/word-pattern/

'''
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty word in str.
Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains
lowercase letters separated by a single space.
'''

# Approach 1:
# time complexity: O(n) - index * O(n) - map = O(n^2)
def wordPattern(self, pattern, str):
   clist = pattern            #treat string as a list of chars
   wlist = str.split()        #split string into a list of words
   # map(function, sequence): map applies the given function to every element in the sequence and returns a list
   # index - finds the index of the first occurence of every element in both list and string
   return list(map(clist.index, clist)) == list(map(wlist.index, wlist))

# Approach 2:
def wordPattern(self, pattern, str):
    clist = pattern
    wlist = str.split()
    # zip returns a tuple, cpupling the ith elements from both lists
    return len(clist) == len(wlist) and len(set(clist)) == len(set(wlist)) == len(set(zip(clist, wlist)))

# "abba", "dog cat cat dog", True.
# "abba", "dog cat cat fish" False.
# "aaaa", "dog cat cat dog"  False.
# "abba", "dog dog dog dog"  False.
