# @file  Valid Perfect Square
# @brief Given a positive integer num, write a function which returns True if num is a perfect square else False.

# https://leetcode.com/problems/valid-perfect-square/

'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
'''

# time complexity: O(sqrt(n))
# space complexity: O(1)


def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(num+1):
            if i * i == num:
                return True
            elif i * i > num:
                break
        return False
