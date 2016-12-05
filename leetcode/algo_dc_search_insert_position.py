# @file  Search insert position
# @brief In a sorted list find position or potential position of a value

# https://leetcode.com/problems/search-insert-position/

'''
Given a sorted array and a target value, return the index if the target
is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

#Lower bound method, let e go beyond bounds
def searchInsert(self, nums, target):
  b, e = 0, len(nums) - 1
  while b <= e:
    mid = b + (e - b) / 2
    if (nums[mid] < target) : b = mid + 1 
    else:                     e = mid - 1
  return b
