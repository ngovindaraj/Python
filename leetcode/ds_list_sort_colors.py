# @file  Sort Colors
# @brief Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# https://leetcode.com/problems/sort-colors/

'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''

# 2-pointer approach
# time: O(n)
# space: O(1)

def sortColors(self, nums):
	b, i, e = 0, 0, len(nums)-1
    while i <= e:
    	if i > b and nums[i] == 0:
        	nums[b], nums[i] = nums[i], nums[b]
        	b += 1
        elif i < e and nums[i] == 2:
            nums[e], nums[i] = nums[i], nums[e]
            e -= 1
        else:
            i += 1
                
# [0]
# [1, 0]
# [2, 0]
# [1, 2, 0]
# [0, 2, 1]
# [0, 1, 2]


