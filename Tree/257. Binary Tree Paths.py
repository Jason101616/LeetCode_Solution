# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# idea: simple dfs solution.

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.findPath(root, res, [])
        return res

    def findPath(self, node, res, prevPath):
        if not node.left and not node.right:
            res.append('->'.join(prevPath + [str(node.val)]))
            return
        if node.left:
            self.findPath(node.left, res, prevPath + [str(node.val)])
        if node.right:
            self.findPath(node.right, res, prevPath + [str(node.val)])
