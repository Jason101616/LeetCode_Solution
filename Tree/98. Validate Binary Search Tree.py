# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1: maintain two variables low_bound and high_bound
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        low_bound = float('-inf')
        high_bound = float('inf')
        return self.is_valid_BST(root, low_bound, high_bound)

    def is_valid_BST(self, node, low_bound, high_bound):
        if not node:
            return True
        if node.val <= low_bound or node.val >= high_bound:
            return False
        return self.is_valid_BST(node.left, low_bound,
                                 node.val) and self.is_valid_BST(
            node.right, node.val, high_bound)


# Solution 2: check whether the inorder traversal is ascending
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.is_valid_BST(root)

    def is_valid_BST(self, node):
        if not node:
            return True
        if not self.is_valid_BST(node.left):
            return False
        if self.prev and node.val <= self.prev.val:
            return False
        self.prev = node
        return self.is_valid_BST(node.right)
