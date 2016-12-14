# @file  Two Sum
# @brief Given an array and target, find 2 nums in array that sum to target

# https://leetcode.com/problems/two-sum/

'''
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.
You may assume that each input would have exactly one solution.
Example: Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

#Note: Use property that if x + y = target, y = target - x
#Use a dictionary with each value (x) as key and idx as value
#Time Complexity = O(n)
def twoSum(self, nums, target):
  dict = {}
  for i in range(len(nums)):
    x = nums[i]
    y = target - x
    if(y in dict):  return dict.get(y), i
    dict[x] = i

