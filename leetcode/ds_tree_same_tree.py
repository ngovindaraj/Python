# @file  Same Tree
# @brief Given 2 BT, do they have same structure and values

# https://leetcode.com/problems/same-tree/

'''
Given two binary trees, write a function to check if they are
equal or not.
Two binary trees are considered equal if they are structurally
identical and the nodes have the same value.
'''

def isSameTree(self, p, q):
  if p is None and q is None:
    return True
  elif p and q:
    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  else:
    return False
        
# [1, 2, 3], [1, 2, 3],  true
# [10,5,15], [10,5,null,null,15],   false
