# @file  Implement Stack using Queues
# @brief Implement the following operations of a stack using queues.

# https://leetcode.com/problems/implement-stack-using-queues/

import collections
'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Notes:
You must use only standard operations of a queue -- which means only push to
back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may
simulate a queue by using a list or deque (double-ended queue), as long as you
use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top
operations will be called on an empty stack).
'''

# time complexity : push = O(n), pop/top = O(1)
# space complexity: O(n)
class MyStack:
    dq_ = None  # Use dequeue as a queue

    def __init__(self):
        self.dq_ = collections.deque()

    def push(self, x):
        self.dq_.appendleft(x)               # Add new element to left
        self.dq_.rotate(len(self.dq_) - 1)   # Bring left most element to right

    def pop(self):
        return self.dq_.pop()

    def top(self):
        return self.dq_[-1]

    def empty(self):
        return len(self.dq_) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
