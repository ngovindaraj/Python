# @file  Valid Parentheses
# @brief Given a string containing just the characters '(', ')', '{', '}',
#        '[' and ']', determine if the input string is valid.

# https://leetcode.com/problems/valid-parentheses/
import collections
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
'''


# time complexity : O(n)
# space complexity: O(n)
def isValid(self, s):
    # Use a dictionary to match fwd and rev brackets
    dct = {'(': ')', '{': '}', '[': ']'}  # HashTable for fwd -> reverse braces
    # For each fwd brace record corresponding reverse brace to match
    stk = collections.deque()
    for char in s:
        if char in dct:                   # If char is fwd bracket
            stk.append(dct[char])         # Append corresponding rev bracket
        elif char in ')}]':               # If char is rev bracket
            if len(stk) == 0:             # Ensure no extra rev brackets
                return False
            elif char != stk.pop():       # Verify rev bracket type
                return False
        else:                             # Found non fwd/rev bracket character
            return False
    return len(stk) == 0                  # Ensure no extra fwd bracket
