# @file  Contains Duplicate II
# @brief Given an array of numbers find if there are any duplicates.
# if yes, check if distance between the duplicates is atmost int k

# https://leetcode.com/problems/contains-duplicate-ii/

'''
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and
the absolute difference between i and j is at most k.
'''

# Brute force - 2 loop approach (complexity: time = O(n^2), space = O(1))
# Note: This is not accepted by leetcode because of high time complexity
def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if len(nums) < 2 or k < 1:
        return False
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                if j - i <= k:
                    return True
    return False


# Dictionary approach (complexity: time = O(n), space = O(n))
def containsNearbyDuplicate2(self, nums, k):
    if len(nums) < 2 or k < 1:
        return False
    dict = {}
    for i in range(len(nums)):
        elem = nums[i]
        if elem in dict:
            if i - dict.get(elem) <= k:
                return True
        dict[elem] = i
    return False
