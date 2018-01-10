# @file  Group Anagrams
# @brief Given an array of strings, group anagrams together.

# https://leetcode.com/problems/group-anagrams/

'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
'''


# time complexity: sort + check + append -> costliest operation: sort -> m being avg length of a string: O(m log m)*n (n being length of all strings)
# space complexity: O(length of strs)

import collections

def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = collections.defaultdict(list)
        for elem in strs:
            dict[''.join(sorted(elem))].append(elem)
        return list(dict.values())
