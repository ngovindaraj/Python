# @file  Same Tree
# @brief Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# https://leetcode.com/problems/symmetric-tree

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
   
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Approach 1: recursively
def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(p, q):
            if p is None and q is None:
                return True
            elif p and q:
                return p.val == q.val and isSym(p.left, q.right) and isSym(p.right, q.left)
            else:
                return False
        return isSym(root, root)
        
# Approach 2: iteratively
def isSymmetric(self, root):
    queue = [root]
    while queue:
        values = [i.val if i else None for i in queue]
        if values != values[::-1]: return False
        queue = [child for i in queue if i for child in (i.left, i.right)]
    return True
