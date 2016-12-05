# @file  First Bad version
# @brief In a list with 2 elements, find the **lower bound** of 2nd element

# https://leetcode.com/problems/first-bad-version/

'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. Since 
each version is developed based on the previous version, all the versions after 
a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad
one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version
is bad. Implement a function to find the first bad version. You should minimize
the number of calls to the API.
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def firstBadVersion(self, n):
  b = 1
  e = n
  while b <= e:
    mid = b + (e-b)/2
    if isBadVersion(mid) == False: b = mid+1 
    else: e = mid-1
    return b
