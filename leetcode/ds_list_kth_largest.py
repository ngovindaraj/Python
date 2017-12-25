# @file  Kth Largest Element in an Array
# @brief Given unsorted array, find kth largest element

# https://leetcode.com/problems/kth-largest-element-in-an-array

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

'''

# Approach 1: quick select
# time complexity: 
# space complexity: 

class Solution(object):
    def partition(self, nums, left, right):
        pivot = nums[left]
        b, e = left + 1, right
        while b <= e:
            if b < pivot: 
                b += 1
            elif e > pivot:
                e -= 1
            else: 
                nums[b], nums[e] = nums[e], nums[b]
                b, e = b + 1, e - 1
        nums[left], nums[e] = nums[e], nums[left]
        print("parition {}" % (e))
        print(nums)
        return e
        
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # binary search like loop to call partition
        b, e = 0, len(nums)-1
        k = len(nums) - k # Convert k from 1-based reverse idx to 0-based fwd idx
        while b <= e:
            pivotPos = self.partition(nums, b, e)
            print("findK {}" % (pivotPos))
            if pivotPos < k:
                b = pivotPos + 1
            elif pivotPos > k:
                e = pivotPos - 1
            else:
                return nums[k] # k = pivotPos
        return -1
 
 
# Approach 2: Each heap operation push/pop is O(log n)
# time: n *log(n)
# space:                 

    def findKthLargest2(self, nums, k):
        heapq.heapify(nums)  #Heapify is a O(n) operation to create a min-heap
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        return heapq.heappop(nums) 
 
 
               
# Approach 3: 
# time: O(n log n), space:

def findKthLargest3(self, nums, k):
    return sorted(nums, reverse=True)[k-1]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
