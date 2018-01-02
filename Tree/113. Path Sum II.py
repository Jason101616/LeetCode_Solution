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

# idea: dfs
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.find_path(root, None, sum, res, [])
        return res
    
    def find_path(self, cur_node, prev_sum, target, res, cur_path):
        if not cur_node:
            return
        if not prev_sum:
            prev_sum = 0
        prev_sum += cur_node.val
        cur_path.append(cur_node.val)
        if not cur_node.left and not cur_node.right and prev_sum == target:
            res.append(copy.deepcopy(cur_path))
        self.find_path(cur_node.left, prev_sum, target, res, cur_path)
        self.find_path(cur_node.right, prev_sum, target, res, cur_path)
        cur_path.pop()