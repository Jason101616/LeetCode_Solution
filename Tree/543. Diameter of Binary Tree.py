# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.longest = 0
    
    # 思路：
    # 经过某个node的最长路径一定是height of left tree + height of right tree
    # 在求节点高度的过程中，顺便更新一个最长路径的全局变量
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.height(root)
        return self.longest

    def height(self, node):
        if not node:
            return 0
        h_l = self.height(node.left)
        h_r = self.height(node.right)
        if h_l + h_r > self.longest:
            self.longest = h_l + h_r
        return max(h_l, h_r) + 1
        