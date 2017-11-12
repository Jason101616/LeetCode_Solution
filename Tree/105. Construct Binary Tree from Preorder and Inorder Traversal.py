# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# idea: preorder can get the root of the current list, inorder can be used to split preorder and inorder to help recursion
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        return self.build_tree(preorder, inorder)

    def build_tree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        new_node = TreeNode(preorder[0])
        in_order_index = inorder.index(preorder[0])
        new_node.left = self.build_tree(preorder[1:1 + in_order_index],
                                        inorder[:in_order_index])
        new_node.right = self.build_tree(preorder[1 + in_order_index:],
                                         inorder[in_order_index + 1:])
        return new_node