# @file  Balanced Binary Tree
# @brief Given a binary tree, determine if it is height-balanced.

# https://leetcode.com/problems/balanced-binary-tree/

'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined
as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

#Given a BT node, find the depth (1-based depth)
def maxDepth(root):
  if (root == None):                               return 0
  elif (root.left == None and root.right == None): return 1
  else:                                            return 1 + max(maxDepth(root.left), maxDepth(root.right))

def isBalanced(self, root):
  if(root == None):                                         return True
  elif abs(maxDepth(root.left) - maxDepth(root.right)) > 1: return False
  elif self.isBalanced(root.left) == False:                 return False
  else:                                                     return self.isBalanced(root.right)
  
