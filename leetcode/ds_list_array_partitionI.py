# @file  Array Partition I
# @brief Given a list of 2n integers, find the max sum from min(n pairs)

# https://leetcode.com/problems/array-partition-i

'''
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).


Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
'''

# Explanation: The intuitive way of reasoning is that, to get the the sum of mins as large as possible, we need to make the min numbers as large as possible. 
# Essentially, we're sacrificing large numbers by grouping them with the small numbers. To make the small numbers as large as possible, the best way is to group them with their adjacent large numbers.
# For example, (1, 3) and (2, 4) are not best pairs since you're sacrificing 3 by grouping it with 1. (1, 2) and (3, 4) is better since now 3 is the MIN and can contribute to the sum.

# Approach 1:
# time complexity: O(n log n): sort + O(n/2): for loop = O(n log n)
# space complexity: O(1): single num storage

def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0
        # for i ..with step 2, creates a list like this: [0,2,4,..]
        for i in range(0,len(nums),2):
            total += nums[i]
        return total


# Approach 2: one-liner
# time complexity: O(n log n), space complexity: O(1)

def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])