# @file  BT Max / Min depth
# @brief Given a Binary Tree find max/min depth

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

'''
Given a binary tree, find its maximum and minimum depth.
- The maximum depth is the number of nodes along the longest path
  from the root node down to the farthest leaf node.
- The minimum depth is the number of nodes along the shortest path
  from the root node down to the nearest leaf node.
'''

#Use recursion to find the max depth of a BT/BST
def maxDepth(self, root):
  if not root:                                     
    return 0
  return 1 + max( self.maxDepth(root.left), self.maxDepth(root.right))

#Iterative solution to find max depth of a BT/BST
    def maxDepth(self, root: TreeNode) -> int:
        st : List[(TreeNode, int)] = []
        max_depth = 0
        if root:
            st.append((root, 1))
        while st:
            (node, cur_depth) = st.pop()
            if node.left:
                st.append((node.left, cur_depth + 1))
            if node.right:
                st.append((node.right, cur_depth + 1))
            max_depth = max(max_depth, cur_depth)
        return max_depth
      
#Use recursion to find the min depth of a BT/BST
def minDepth(self, root):
  if not root               : return 0
  elif (root.left  == None) : return 1 + self.minDepth(root.right)
  elif (root.right == None) : return 1 + self.minDepth(root.left)
  else: return 1 + min(map(self.minDepth,(root.left, root.right)))

  
