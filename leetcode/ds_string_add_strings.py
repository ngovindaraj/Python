# @file  Add Strings
# @brief Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2

# https://leetcode.com/problems/add-strings/

'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

# time: O(length of biggest string)
# space: O(length of biggest string)

 def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        ans = ""
        for tup in itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            sum = int(tup[0]) + int(tup[1]) + carry
            ans = str(sum % 10) + ans
            carry = int(sum / 10)
        if carry:
            ans = str(carry) + ans
        return ans