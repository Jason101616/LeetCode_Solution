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
# idea: first put the preorder traversal in a list, than wire each node
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inorder_node_list = []
        self.inorder_traverse(root)
        len_inorder = len(self.inorder_node_list)
        for i in range(len_inorder - 1):
            self.inorder_node_list[i].left = None
            self.inorder_node_list[i].right = self.inorder_node_list[i + 1]

    def inorder_traverse(self, node):
        if node:
            self.inorder_node_list.append(node)
            self.inorder_traverse(node.left)
            self.inorder_traverse(node.right)


# Solution 2:
# idea: better solution, use a stack to simulate pre-order traversal
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        prev_node = TreeNode(None)
        stack = [root]
        while stack:
            top = stack.pop()
            if not top:
                continue
            stack.append(top.right)
            stack.append(top.left)
            prev_node.right = top
            prev_node.left = None
            prev_node = top