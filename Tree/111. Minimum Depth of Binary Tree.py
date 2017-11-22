# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# idea: DFS
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.shortest = float('inf')
        self.find_min_depth(root, 1)
        return self.shortest

    def find_min_depth(self, node, cur_depth):
        if not node:
            return
        if not node.left and not node.right:
            if cur_depth < self.shortest:
                self.shortest = cur_depth
            return
        self.find_min_depth(node.left, cur_depth + 1)
        self.find_min_depth(node.right, cur_depth + 1)