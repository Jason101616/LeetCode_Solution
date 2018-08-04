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

# idea: iterative approach, the node in the left side of the root is smaller than root
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        left_cnt = self.cnt_node(root.left)
        if left_cnt == k - 1:
            return root.val
        elif left_cnt >= k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - left_cnt - 1)

    def cnt_node(self, root):
        if not root:
            return 0
        return self.cnt_node(root.left) + self.cnt_node(root.right) + 1
