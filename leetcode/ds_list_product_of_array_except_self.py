# @file  Product of Array Except Self
# @brief Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# https://leetcode.com/problems/product-of-array-except-self/

'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

'''

# 2-pointer approach
# time complexity: O(n)
# space: O(1) -- excluding 'ans'
def productExceptSelf(self, nums):
        ans = [1] * len(nums)
        fm, rm = 1, 1
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            ans[i] *= fm
            ans[j] *= rm
            fm *= nums[i]
            rm *= nums[j]
        return ans
