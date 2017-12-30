# @file  Top K Frequent Elements
# @brief Given a non-empty array of integers, return the k most frequent elements.

# https://leetcode.com/problems/top-k-frequent-elements/

'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

import collections
import heapq


# Approach 1 : Use dictionary + Max-Heap
# Time complexity : O(n) + O(k log n)
# Space complexity : O(n)
def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dict = collections.Counter(nums)
    # Note: for a dictionary, sorted, nlargest, etc returns keys (not values)
    return heapq.nlargest(k, dict, key=lambda x: dict[x])


# Approach 2 : Use Counter inbuilt heap function and use list comprehension
# Time complexity : O(n) + O(k log n)
# Space complexity : O(n)
def topKFrequent2(self, nums, k):
    return [i[0] for i in collections.Counter(nums).most_common(k)]


# Approach 3: Use dictionary for counter, sort by value and pick top k
# Time complexity : O(n) + O(n log n)
# Space complexity : O(n)
def topKFrequent3(self, nums, k):
    dict = collections.Counter(nums)
    return sorted(dict, reverse=True, key=lambda x: dict[x])[:k]
