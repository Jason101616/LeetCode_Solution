# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1: recursive
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.is_symmetric(root.left, root.right)

    def is_symmetric(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.is_symmetric(node1.left,
                                 node2.right) and self.is_symmetric(
            node1.right, node2.left)


# Solution 2: iteratively
from collections import deque


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q1 = deque()
        q2 = deque()
        q1.append(root.left)
        q2.append(root.right)
        while q1 and q2:
            cur_1 = q1.popleft()
            cur_2 = q2.popleft()
            if not cur_1 and not cur_2:
                continue
            if cur_1 and not cur_2 or not cur_1 and cur_2 or cur_1.val != cur_2.val:
                return False
            q1.append(cur_1.right)
            q1.append(cur_1.left)
            q2.append(cur_2.left)
            q2.append(cur_2.right)
        return True
