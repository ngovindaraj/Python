# @file  Add Binary
# @brief Given two binary strings, return their sum (also a binary string).

# https://leetcode.com/problems/add-binary/

'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

# time: O(length of biggest string)
# space: O(length of biggest string)

 def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        ans = ""
        for tup in itertools.zip_longest(a[::-1], b[::-1], fillvalue='0'):
            sum = int(tup[0]) + int(tup[1]) + carry
            ans = str(sum % 2) + ans
            carry = int(sum / 2)
        if carry:
            ans = str(carry) + ans
        return ans