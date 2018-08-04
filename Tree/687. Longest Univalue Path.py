# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

# Note: The length of path between two nodes is represented by the number of edges between them.

# Example 1:

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:

# 2
# Example 2:

# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:

# 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# idea: recursion. Calculate node number first, then minus 1.
class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.longest_path = 0
        self.find_longest(root)
        return self.longest_path - 1

    def find_longest(self, node):
        if not node:
            return 0
        left_len = self.find_longest(node.left)
        right_len = self.find_longest(node.right)
        cur_len_0 = cur_len_1 = 1
        if node.left and node.val == node.left.val:
            cur_len_0 += left_len
        if node.right and node.val == node.right.val:
            cur_len_1 += right_len
        self.longest_path = max(self.longest_path, cur_len_0 + cur_len_1 - 1)
        return max(cur_len_0, cur_len_1)
