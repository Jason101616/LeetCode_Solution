# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1: according to definition
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_height = self.cal_height(root.left)
        right_height = self.cal_height(root.right)
        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def cal_height(self, node):
        if not node:
            return 0
        return max(self.cal_height(node.left), self.cal_height(node.right)) + 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 2: in the dfs process, check the height of each subtree

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)[0]

    def helper(self, node):
        if not node:
            return True, 0
        leftBalanced, leftHeight = self.helper(node.left)
        if not leftBalanced:
            return False, 0
        rightBalanced, rightHeight = self.helper(node.right)
        if not rightBalanced:
            return False, 0
        if abs(leftHeight - rightHeight) > 1:
            return False, 0
        return True, max(leftHeight, rightHeight) + 1