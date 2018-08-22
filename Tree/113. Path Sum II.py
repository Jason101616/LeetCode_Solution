# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# idea: dfs, top-bottom
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.helper(root, res, sum, [root.val])
        return res

    def helper(self, node, res, target, curRes):
        if not node.left and not node.right:
            if sum(curRes) == target:
                res.append(curRes)
            return
        if node.left:
            self.helper(node.left, res, target, curRes + [node.left.val])
        if node.right:
            self.helper(node.right, res, target, curRes + [node.right.val])