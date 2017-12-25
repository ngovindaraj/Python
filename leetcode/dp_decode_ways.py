# @file  Decode Ways
# @brief Given an encoded message containing digits, determine the total number of ways to decode it.

# https://leetcode.com/problems/decode-ways

'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

# Dynamic Programming
# time complexity: O(n) - going through list once
# space: O(n) -- the dp list


def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dp[i] = dp[i-1] if s[i] != "0"
        #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
        if s == "": return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
                dp[i] += dp[i-2]
            print(i)
            print(dp)
        return dp[len(s)]
        
# "0" = 0
# "00" = 0
# "1" = 1
# "12" = 2
# "10" = 1
# "11" = 2
# "111" = 3
# "10100" = 0
# "11012" = 2
