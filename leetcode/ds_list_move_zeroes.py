# @file  Move Zeroes
# @brief Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# https://leetcode.com/problems/move-zeroes/

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

# 2-pointer approach
# time: O(n)
# space: O(1)

def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonzeroIdx = 0  # Non-zero boundary
        for v in range(1, len(nums)):
            if nums[nonzeroIdx] != 0:  # Increase non-zero boundary
                nonzeroIdx += 1
            nums[nonzeroIdx] = nums[v]
        nums[nonzeroIdx +1 : len(nums)] = [0] * (len(nums) - (nonzeroIdx +1))


