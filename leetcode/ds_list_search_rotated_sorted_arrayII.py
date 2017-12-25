# @file  Search in Rotated Sorted ArrayII
# @brief Given a sorted rotated array, search for target

# https://leetcode.com/problems/search-in-rotated-sorted-array-ii

'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
'''

# avg time complexity: O(log n), worst case time complexity: O(n) - if everything is a duplicate
# space complexity: O(1)
def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        b, e = 0, len(nums)-1
        while b <= e:
            mid = b + (e-b)/2
            if nums[mid] == target:
                return True
            if nums[b] < nums[mid]:
                if target >= nums[b] and target < nums[mid]:
                    e = mid - 1
                else: 
                    b = mid + 1
            elif nums[mid] < nums[e]:
                if target <= nums[e] and target >= nums[mid]:
                    b = mid + 1
                else:
                    e = mid - 1
            elif nums[b] != target:
                    b += 1
            else: 
                e -= 1
        return False
