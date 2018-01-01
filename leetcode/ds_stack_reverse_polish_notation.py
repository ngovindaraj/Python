# @file  Evaluate Reverse Polish Notation
# @brief Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# https://leetcode.com/problems/evaluate-reverse-polish-notation/
import collections
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another
expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''


# time complexity : O(n)
# space complexity: O(n)
def evalRPN(self, tokens):
    stack = collections.deque()  # Use a stack to store numbers
    for elem in tokens:          # Go over each number / operator
        # If not operator, treat as int. This handles -ve numbers as well
        if elem not in "+-*/":
            stack.append(int(elem))
        else:  # If this is an operator, pop last 2 numbers and operate
            second_num = stack.pop()
            first_num = stack.pop()
            if elem == '+':
                stack.append(first_num + second_num)
            elif elem == '-':
                stack.append(first_num - second_num)
            elif elem == '*':
                stack.append(first_num * second_num)
            elif elem == '/':
                stack.append(int(first_num / second_num))
    return stack.pop()
