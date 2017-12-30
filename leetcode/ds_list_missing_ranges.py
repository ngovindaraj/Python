# @file  Missing Ranges
# @brief Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

# https://leetcode.com/problems/missing-ranges/

'''
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

'''

# 2-pointer approach
# time complexity: O(n)
# space: O(1)


def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        result = []
        for i in range(len(nums)-1):
            b, e = nums[i], nums[i+1]
            if e - b == 2:  
            	result.append(str(e-1))
            elif e - b > 2: 
            	result.append(str(b+1) + '->' + str(e-1))
        return result
