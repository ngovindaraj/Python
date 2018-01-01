# @file  Implement Queue using Stacks
# @brief Implement the following operations of a queue using stacks.

# https://leetcode.com/problems/implement-queue-using-stacks/
import collections
'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Notes:
You must use only standard operations of a stack -- which means only push to
top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may
simulate a stack by using a list or deque (double-ended queue), as long as you
use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek
operations will be called on an empty queue).
'''


# time complexity : push = O(1), pop/peek = O(n)
# space complexity: O(n)
class MyQueue:
    eStack, dStack = None, None  # Use eStack for push and dStack for pop

    def __init__(self):
        self.eStack, self.dStack = collections.deque(), collections.deque()

    def push(self, x):
        self.eStack.append(x)

    def pop(self):
        self.peek()
        return self.dStack.pop()

    def peek(self):
        # To preserve stack order, only move elements if dStack is empty
        if len(self.dStack) == 0:
            while len(self.eStack):  # Move all elements from eStack to dStack
                self.dStack.append(self.eStack.pop())
        return self.dStack[-1]

    def empty(self):  # Remember to check if both stacks are empty
        return len(self.dStack) == 0 and len(self.eStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
