# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# idea: preorder can get the root of the current list, inorder can be used to split preorder and inorder to help recursion
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        newNode = TreeNode(preorder[0])
        inOrderIdx = inorder.index(preorder[0])
        newNode.left = self.buildTree(preorder[1:1 + inOrderIdx], inorder[:inOrderIdx])
        newNode.right = self.buildTree(preorder[1 + inOrderIdx:], inorder[inOrderIdx + 1:])
        return newNode
