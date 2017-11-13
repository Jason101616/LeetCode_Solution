# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# idea: in-order traversal, find the two problematic node and change their value
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.prev_node = None
        self.problem_node_0 = None
        self.problem_node_1 = None
        self.last_visit = None
        self.recover(root)
        if not self.problem_node_1:
            self.problem_node_0.val, self.last_visit.val = self.last_visit.val, self.problem_node_0.val

    def recover(self, cur_node):
        if cur_node:
            self.recover(cur_node.left)
            self.last_visit = cur_node
            if not self.prev_node:
                self.prev_node = cur_node
            else:
                if not self.problem_node_0:
                    if self.prev_node.val > cur_node.val:
                        self.problem_node_0 = self.prev_node
                if self.problem_node_0 and not self.problem_node_1:
                    if cur_node.val > self.problem_node_0.val and self.prev_node.val < self.problem_node_0.val:
                        self.problem_node_1 = self.prev_node
                    if self.problem_node_0 and self.problem_node_1:
                        self.problem_node_0.val, self.problem_node_1.val = self.problem_node_1.val, self.problem_node_0.val
                        return
                self.prev_node = cur_node
            self.recover(cur_node.right)
