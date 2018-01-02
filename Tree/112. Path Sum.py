# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# idea: dfs
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.ans = False
        self.find_path(root, None, sum)
        return self.ans
    
    def find_path(self, cur_node, prev_sum, target):
        if not cur_node:
            return
        if not prev_sum:
            prev_sum = 0
        prev_sum += cur_node.val
        if not cur_node.left and not cur_node.right and prev_sum == target:
            self.ans = True
        self.find_path(cur_node.left, prev_sum, target)
        self.find_path(cur_node.right, prev_sum, target)