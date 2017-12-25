# @file  Length of Last Word
# @brief Given a string, return length of last word

# https://leetcode.com/problems/length-of-last-word/

'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

'''

# Approach 1: for loop
# time complexity: worst case: O(n)
# space: O(1)

def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if length == 0: continue
                else: break
            else:       			# this is a word character, increase length
                length += 1   
        return length 

# Approach 2: using predefined functions
# time: O(n)
# space: O(n)

def lengthOfLastWord(self, s):
	word_lst = s.split()
	if len(word_lst):
     	return len(word_lst[-1])
	return 0