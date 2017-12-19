# @file  Single Number
# @brief Find the unique integer given array of re-occuring integers

# https://leetcode.com/problems/single-number/

'''
Given an array of integers, every element appears twice except for one.
Find that single one.
Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
'''

# Approach 1: Use a dictionary with the following operations:
# - If elem not in dictionary (1st occur), add it to dictionary
# - If elem in dictionary (2nd occurence), remove it from dictionary
# The only element left in dictionary is the non-duplicate number
# Time Complexity = O(n)
def singleNumber(self, nums):
  dict = {}
  for val in nums:
    if val not in dict: dict[val] = 1
    else:               del dict[val]
  #Only element left in dictionary is the single number
  for key in dict:      return key

  # Approach 2: lambda operator with reduce function - without using extra memory
  # x ^ y - Does a "bitwise exclusive or"
  def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
