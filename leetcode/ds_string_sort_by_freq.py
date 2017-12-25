# @file  Sort Characters By Frequency
# @brief Given a string, sort it in decreasing order based on the frequency of characters.

# https://leetcode.com/problems/sort-characters-by-frequency

'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

# time complexity: O(length of str) + O(length of dict) = O(2n) = O(n)
# space complexity: O(len of dict - at most len of str) + O(len of str) = O(2n) = O(n)

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        word = ""
        for elem in s:
            dict[elem] = dict.get(elem, 0) + 1
        for k, v in sorted(dict.iteritems(), key=lambda x: x[1], reverse = True):
            word += ''.join(k*v)
        return word
        
                
