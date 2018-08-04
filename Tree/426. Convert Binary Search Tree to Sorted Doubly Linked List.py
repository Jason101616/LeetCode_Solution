# Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

# Let's take the following BST as an example, it may help you understand the problem better:


# We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.


# Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

# The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

# Idea:
# First implement a BST iterator (problem 173). Then the problem is very easy, just be careful to the corner case

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.fillStack(root, self.stack)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def next(self):
        """
        :rtype: Node
        """
        node = self.stack.pop()
        self.fillStack(node.right, self.stack)
        return node

    def fillStack(self, node, stack):
        while node:
            stack.append(node)
            node = node.left


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        bstIterator = BSTIterator(root)
        root = prevNode = bstIterator.next()
        while bstIterator.hasNext():
            curNode = bstIterator.next()
            prevNode.right = curNode
            curNode.left = prevNode
            prevNode = curNode
        root.left = prevNode
        prevNode.right = root
        return root
