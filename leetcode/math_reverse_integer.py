# @file  Math Reverse Integer
# @brief Given a 32-bit signed integer, reverse digits of an integer.


# https://leetcode.com/problems/reverse-integer/


'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within
the 32-bit signed integer range. For the purpose of this problem, assume that
your function returns 0 when the reversed integer overflows.

'''

# Approach 1: Math
# time: O(n)
# space:

def reverse(self, x):
    maxInt = 2**31-1   # Maximum positive integer
    ans = 0
    sign = -1 if x < 0 else 1
    x = sign * x       # Convert negative x to positive x
    while x:
        x, lastDigit = x // 10, x % 10
        # ans = ans * 10 + lastDigit (with overflow checks)
        # Do ans = ans * 10 while checking for overflow (a * b <= max ---- a <= max / b)
        if ans   <= maxInt // 10:
            ans *= 10
        else:
            return 0
        # Do ans += lastDigit while checking overflow (a + b <= max ---- a <= max - b)
        if ans <= maxInt - lastDigit:
            ans += lastDigit
        else:
            return 0
    return sign * ans
