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

# idea: top to bottom dfs
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.find_path(root, 0, sum)
    
    def find_path(self, cur_node, prev_sum, target):
        if not cur_node:
            return False
        cur_sum = prev_sum + cur_node.val
        if not cur_node.left and not cur_node.right and cur_sum == target:
            return True
        return self.find_path(cur_node.left, cur_sum, target) or self.find_path(cur_node.right, cur_sum, target)
        