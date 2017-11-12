# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# idea: DFS search or backtracing
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = float('-inf')
        self.find_max(root)
        return self.max

    def find_max(self, node):
        if not node:
            return 0
        left = max(self.find_max(node.left), 0)
        right = max(self.find_max(node.right), 0)
        if left + right + node.val > self.max:
            self.max = left + right + node.val
        return max(left, right) + node.val
