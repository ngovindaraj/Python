# @file  Minimum Size Subarray Sum
# @brief Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# https://leetcode.com/problems/minimum-size-subarray-sum/

'''
Given an array of n positive integers and a positive integer s, find the minimal
length of a contiguous subarray of which the sum ≥ s. If there isn't one,
return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which
the time complexity is O(n log n).
'''


# Dynamic moving window (expand and shrink) approach
# time complexity: O(n)
# space: O(1)
def minSubArrayLen(self, s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    b, sum, min_length = 0, 0, 0
    for e in range(len(nums)):  # Increase the boundary in each iteration
        sum = sum + nums[e]
        if sum >= s:       # A successful boundary found
            # See if we can shrink the boundary first.
            while (sum - nums[b]) >= s:
                sum -= nums[b]
                b += 1
            # If this is the first or lowest window, then record this
            if min_length is 0 or e - b + 1 < min_length:
                min_length = e - b + 1
    return min_length
