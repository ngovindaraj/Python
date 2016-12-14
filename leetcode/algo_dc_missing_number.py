# @file  Find Missing Number
# @brief Given unsorted array of n distinct numbers from 0-n, find a missing number

# https://leetcode.com/problems/missing-number/

'''
Given an unsorted array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.
'''
#Approach 1: Divide and Conquer (lower bound BS based)
#Time Complexity = O(log n)
def missingNumber(self, nums):
  nums.sort()
  b, e = 0, len(nums) - 1
  while b <= e:
    mid = b + (e - b) / 2
    if mid == nums[mid]: b = mid + 1
    else:                e = mid - 1
  return b
    
#Approach 2: For-loop + math based (https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF)
#Missing number is difference between expected sum and calculated sum
#Time Complexity = O(n)
def missingNumber(self, nums):
  n = len(nums) + 1         #n = total num of elems =  #elems in array + 1 missing element
  n = n - 1                 #nums is 0-based and not 1-based for summation series
  exp_sum = n * (n + 1) / 2 #sum calculated with summation series formula
  act_sum = sum(nums)       #actual sum of the array (this is a O(n) for-loop)
  return exp_sum - act_sum

#Test-cases
# [0],           1
# [1],           0
# [0, 1, 2]      3
# [0, 2, 3]      1
