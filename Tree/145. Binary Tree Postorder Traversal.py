# Given a binary tree, return the postorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [3,2,1]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Easiest version:
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if node:
            self.helper(node.left, res)
            self.helper(node.right, res)
            res.append(node.val)


# stack version:
from collections import deque


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = deque()
        stack = []
        while root or stack:
            if root:
                res.appendleft(root.val)
                stack.append(root)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return list(res)
