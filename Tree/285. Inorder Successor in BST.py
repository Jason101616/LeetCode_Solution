# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

# Note: If the given node has no in-order successor in the tree, return null.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Approach 1: Use in-order traversal, when find p, mark a global varible. Next time when detect that global variable,
# return the current node directly.
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.find_node = False
        self.suc = None
        self.inorder(root, p)
        return self.suc

    def inorder(self, node, target):
        if node:
            self.inorder(node.left, target)
            if self.find_node and self.suc == None:
                self.suc = node
                return
            if node == target:
                self.find_node = True
            self.inorder(node.right, target)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Approach 2: check recursively
# 当根结点值小于等于p结点值，说明p的后继结点一定在右子树中，所以对右子结点递归调用此函数，如果根结点值大于p结点值，那么有可能根结点就是p的后继结点，或者左子树中的某个结点是p的后继结点，所以先对左子结点递归调用此函数，如果返回空，说明根结点是后继结点，返回即可，如果不为空，则将那个结点返回
# time: O(logn), space: O(logn)
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val > p.val:
            res = self.inorderSuccessor(root.left, p)
            return res if res else root
        elif root.val <= p.val:
            return self.inorderSuccessor(root.right, p)


# Approach 3: check iteratively
# time: O(logn), space: O(1)
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        res = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                res = root
                root = root.left
        return res
