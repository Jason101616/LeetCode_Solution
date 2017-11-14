# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# idea: use the attibute of BST, the node in the left tree of current node is smaller than current node
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0
        self.ans = None
        self.find = False
        self.find_k_small(root, 0, k)
        return self.ans

    def find_k_small(self, node, cur_small, target):
        if not node:
            return cur_small
        left_small = self.find_k_small(node.left, cur_small, target)
        new_small = left_small + 1
        if new_small == target and not self.find:
            self.ans = node.val
            self.find = True
            return 0
        right = self.find_k_small(node.right, new_small, target)
        return right
