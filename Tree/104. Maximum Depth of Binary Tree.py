# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Solution 1: DFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 0
        self.find_max(root, 0)
        return self.max

    def find_max(self, node, length):
        if not node:
            if length > self.max:
                self.max = length
            return
        self.find_max(node.left, length + 1)
        self.find_max(node.right, length + 1)


# Solution 2: BFS
from collections import deque


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max = 0
        queue = deque()
        queue.append(root)
        while queue:
            max += 1
            current_len = len(queue)
            for i in range(current_len):
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return max
