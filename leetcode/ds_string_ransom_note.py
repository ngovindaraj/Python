# @file  Ransom Note
# @brief Given a list of 2n integers, find the max sum from min(n pairs)

# https://leetcode.com/problems/ransom-note

'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

# Approach 1:
# time complexity: O(m+n)
# space complexity: 2 dictionaries

# eg. ransomNote='aa', magazine='aab': returns {'a':2} - {'a': 2, 'b':1}
def canConstruct(self, ransomNote, magazine):
    return not collections.Counter(ransomNote) - collections.Counter(magazine)
    
#Approach 2    
    
def canConstruct(self, ransomNote, magazine):    
    	ransDict, magDict = {}, {}
        for elem in ransomNote:
            ransDict[elem] = ransDict.get(elem, 0) + 1
        for elem in magazine:
            magDict[elem] = magDict.get(elem, 0) + 1
        for k, v in ransDict.items():  
            if magDict.get(k, 0) < v:
                return False
        return True


