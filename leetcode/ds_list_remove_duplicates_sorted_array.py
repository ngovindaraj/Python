# @file  Remove Duplicates from Sorted Array
# @brief Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''

# 2-pointer approach
# time: O(n)
# space: O(1)

 def removeDuplicates(self, nums):
        uniqIdx = 0  # Unique boundary
        for v in range(1, len(nums)):
            if nums[uniqIdx] != nums[v]:  # Increase uniq boundary
                uniqIdx += 1
                nums[uniqIdx] = nums[v]
        return uniqIdx + bool(len(nums))  # Length of the unique boundary


