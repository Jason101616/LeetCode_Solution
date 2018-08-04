# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# a. Naive idea is:
# can be divided into 3 circumstances:
# 1. has right subtree
# 2. do not has right sub and cur == parent.left
# 3. hasNext return False

# b. A further idea:
# use inorder traversal, print the answer one by one
# the problem is that it use more than O(h) space

# c. Use a stack record the node in left subtree
# if this stack is not empty, then hasNext is True
# next is the top node of the stack
# each time invoke next function, we should update the stack

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution c
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self.fill_stack(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def next(self):
        """
        :rtype: int
        """
        cur_node = self.stack.pop()
        self.fill_stack(cur_node.right)
        return cur_node.val

    def fill_stack(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# Solution b:
from collections import deque


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.queue = deque()
        self.inorder_traversal(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue

    def next(self):
        """
        :rtype: int
        """
        cur_node = self.queue.popleft()
        return cur_node.val

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            self.queue.append(node)
            self.inorder_traversal(node.right)
