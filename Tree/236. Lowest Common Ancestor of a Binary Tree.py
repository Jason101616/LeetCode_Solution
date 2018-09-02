# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# this code can resolve the problem of cannot distinguish between p is a child of q and p is in the tree but q is not
# return two values, one is the potential common ancester, the other is the flag indicating whether this node is the real LCA
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node, res = self.helper(root, p, q)
        return node if res else None

    def helper(self, node, p, q):
        if not node:
            return None, False
        if node == p and node == q:
            return node, True

        lNode, isLeft = self.helper(node.left, p, q)
        if isLeft:
            return lNode, True
        rNode, isRight = self.helper(node.right, p, q)
        if isRight:
            return rNode, True

        if node == p or node == q:
            return (node, True) if lNode or rNode else (node, False)

        if lNode and rNode:
            return node, True
        elif lNode or rNode:
            return (lNode, False) if lNode else (rNode, False)
        else:
            return None, False