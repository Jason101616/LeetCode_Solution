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
        node, res = self.LCAhelper(root, p, q)
        return node if res else None

    def LCAhelper(self, root, p, q):
        # base case
        if not root:
            return None, False
        if root == p and root == q:
            return root, True

        # already find the answer in one side
        l_node, is_left = self.LCAhelper(root.left, p, q)
        if is_left:
            return l_node, True
        r_node, is_right = self.LCAhelper(root.right, p, q)
        if is_right:
            return r_node, True

        # current node is p or q, we should check whether we have find q or p in one of the child
        if root == p or root == q:
            return (root, True) if l_node or r_node else (root, False)

        # find one node in one or two sides or non of the sides
        if l_node and r_node:
            return root, True
        elif l_node or r_node:
            return (l_node, False) if l_node else (r_node, False)
        else:
            return None, False
