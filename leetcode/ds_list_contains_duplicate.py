# @file  Contains Duplicate
# @brief Given an array of numbers find if there are any duplicates

# https://leetcode.com/problems/contains-duplicate/

'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.
'''


# Dictionary approach (time_complexity = O(n), space_complexity = O(n))
def containsDuplicate(self, nums):
    dict = {}
    for elem in nums:
        dict[elem] = dict.get(elem, 0) + 1
        if dict[elem] > 1:
            return True
    return False
