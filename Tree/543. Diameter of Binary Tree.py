# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# idea: simple recursion
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.longest = 0
        self.find_longest(root)
        return self.longest - 1

    def find_longest(self, node):
        if not node:
            return 0
        left_len = self.find_longest(node.left)
        right_len = self.find_longest(node.right)
        self.longest = max(self.longest, right_len + left_len + 1)
        return max(left_len, right_len) + 1
