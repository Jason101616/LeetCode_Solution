# Given a binary tree, find the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# idea: recursive. easy
class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        self.find_longest(root)
        return self.longest
    
    def find_longest(self, node):
        if not node:
            return 0
        left_len = self.find_longest(node.left)
        right_len = self.find_longest(node.right)
        cur_len_left = cur_right_len = 1
        if node.left and node.left.val - node.val == 1:
            cur_len_left += left_len
        if node.right and node.right.val - node.val == 1:
            cur_right_len += right_len
        cur_longest = max(self.longest, cur_len_left, cur_right_len)
        if cur_longest > self.longest:
            self.longest = cur_longest
        return max(cur_len_left, cur_right_len)
    