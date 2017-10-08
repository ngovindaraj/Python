# @file  Contains Duplicate
# @brief Given an array of numbers find if there are any duplicates

# https://leetcode.com/problems/contains-duplicate/

'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.
'''


# Brute force - 2 loop approach (complexity: time = O(n^2), space = O(1))
# Note: This is not accepted by leetcode because of high time complexity
def containsDuplicate1(self, nums):
    if len(nums) < 2:
        return False
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# Sort approach (complexity: time = O(n log n), space = O(1))
def containsDuplicate2(self, nums):
    if len(nums) < 2:  #if num elements is less than 2, no duplicates
        return False
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False


# Dictionary approach (complexity: time = O(n), space = O(n))
def containsDuplicate3(self, nums):
    dict = {}
    for elem in nums:
        dict[elem] = dict.get(elem, 0) + 1
        if dict[elem] > 1:
            return True
    return False


# Set approach  (complexity: time = O(n), space = O(n))
def containsDuplicate4(self, nums):
    return len(nums) != len(set(nums))
