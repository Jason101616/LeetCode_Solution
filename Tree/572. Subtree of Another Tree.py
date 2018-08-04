# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# idea: For each node during pre-order traversal of s, use a recursive function isIdentical to validate if subtree started with current node is the same with t.
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if self.isIdentical(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isIdentical(self, node0, node1):
        if not node0 and not node1:
            return True
        if not node0 or not node1 or node0.val != node1.val:
            return False
        return self.isIdentical(node0.left, node1.left) and self.isIdentical(node0.right, node1.right)
