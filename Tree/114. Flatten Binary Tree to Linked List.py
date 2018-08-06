# Given a binary tree, flatten it to a linked list in-place.

# For example,
# Given

#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1:
# idea: first put the preorder traversal into a list, than build the flattened tree
class Solution(object):
    def __init__(self):
        self.inorderNode = []

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inorderTraverse(root)
        for i in range(len(self.inorderNode) - 1):
            self.inorderNode[i].left = None
            self.inorderNode[i].right = self.inorderNode[i + 1]

    def inorderTraverse(self, node):
        if node:
            self.inorderNode.append(node)
            self.inorderTraverse(node.left)
            self.inorderTraverse(node.right)


# Solution 2:
# idea: better solution, use a stack to simulate pre-order traversal
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        prevNode = TreeNode(None)
        stack = [root]
        while stack:
            top = stack.pop()
            if not top:
                continue
            stack.append(top.right)
            stack.append(top.left)
            prevNode.right = top
            prevNode.left = None
            prevNode = top

# recursive solution
class Solution(object):
    def __init__(self):
        self.prevNode = TreeNode(None)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)

    def helper(self, node):
        if not node:
            return
        self.prevNode.left = None
        self.prevNode.right = node
        self.prevNode = node
        tmp = node.right
        self.helper(node.left)
        self.helper(tmp)
