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
  if p == None or q == None : return p == q
  elif p.val != q.val       : return False
  elif self.isSameTree(p.left, q.left) == False: return False
  else:                       return self.isSameTree(p.right, q.right)
        
# [1, 2, 3], [1, 2, 3],  true
# [10,5,15], [10,5,null,null,15],   false
