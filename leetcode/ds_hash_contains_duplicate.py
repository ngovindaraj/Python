# @file  Contains Duplicate
# @brief Given array of integers, find if array contains duplicates

# https://leetcode.com/problems/contains-duplicate/

'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in
the array, and it should return false if every element is distinct.
'''

#Use a dictionary to store all numbers. If a number is seen 2nd time return immediately
#Time Complexity = O(n)   since we have a single for-loop to look at all numbers
def containsDuplicate(self, nums):
  dict = {}
  for num in nums:
    if num not in dict:  dict[num] = 1
    elif num   in dict:  return True
  return False

