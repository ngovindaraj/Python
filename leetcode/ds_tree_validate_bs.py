# @file  Validate Binary Search Tree
# @brief Given a binary tree, check if it is a valid binary search tree (BST).

# https://leetcode.com/problems/validate-binary-search-tree

'''
Assume a BST is defined as follows:
Left subtree of a node contains only nodes with keys lesser than node's key.
Right subtree of a node contains only nodes with keys greater than node's key.
Both the left and right subtrees must also be binary search trees.
'''


def isValidBST(self, root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return (self.isValidBST(root.left,  min_val,  root.val) and
            self.isValidBST(root.right, root.val, max_val))
