'''
 @file  Math Shuffle an Array
 @brief Given a set of numbers without duplicates (shuffle them)
'''

# https://leetcode.com/problems/shuffle-an-array/


'''
 Shuffle a set of numbers without duplicates.
 Example:
 // Init an array with set 1, 2, and 3.
 int[] nums = {1,2,3};
 Solution solution = new Solution(nums);
 // Shuffle the array [1,2,3] and return its result.
 Any permutation of [1,2,3] must equally likely to be returned.
 solution.shuffle();
 // Resets the array back to its original configuration [1,2,3].
 solution.reset();
 // Returns the random shuffling of array [1,2,3].
 solution.shuffle();
'''

import random
class Solution(object):

    def __init__(self, nums):
        self.nums = nums
        

    def reset(self):
       return self.nums
        

    def shuffle(self):
        new_nums = copy.deepcopy(self.nums)
        for i in range(len(new_nums)-1, 0, -1):
            r = random.randrange(0, i+1)
            new_nums[i], new_nums[r] = new_nums[r], new_nums[i]
        return new_nums 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
