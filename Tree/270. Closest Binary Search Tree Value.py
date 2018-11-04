# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: 4

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive:
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closestNodeVal = root.val
        self.helper(root, target)
        return self.closestNodeVal

    def helper(self, node, target):
        if not node:
            return
        if abs(node.val - target) < abs(self.closestNodeVal - target):
            self.closestNodeVal = node.val
        if node.val > target:
            self.helper(node.left, target)
        else:
            self.helper(node.right, target)


# iterative:
# Time: O(h), Space: O(1)
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closestNodeVal = root.val
        closestVal = float('inf')
        while root:
            if abs(root.val - target) < closestVal:
                closestNodeVal = root.val
                closestVal = abs(root.val - target)
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return closestNodeVal