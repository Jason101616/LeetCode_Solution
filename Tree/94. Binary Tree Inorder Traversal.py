# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# iterative solution: use a stack
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        stack = []
        cur_node = root
        while stack or cur_node:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            ans.append(cur_node.val)
            cur_node = cur_node.right
        return ans


# recursive solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.in_traversal(root)
        return self.ans

    def in_traversal(self, node):
        if node:
            self.in_traversal(node.left)
            self.ans.append(node.val)
            self.in_traversal(node.right)
