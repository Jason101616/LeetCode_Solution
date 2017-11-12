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


# idea: if find one of the node in left subtree and one in right subtree, return root
# if find one in left subtree but not right subtree, return left subtree
# if find one in right subtree but not left subtree, return right subtree
# if in both subtree find nothing, return None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and right:
            return right
        elif not right and left:
            return left
        elif left and right:
            return root
        elif not left and not right:
            return None


# Solution 2: DFS
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.ans = None
        self.find = False
        self.find_LCA(root, p, q)
        return self.ans

    def find_LCA(self, cur, p, q):
        if not cur:
            return False, False
        find_p_left, find_q_left = self.find_LCA(cur.left, p, q)
        find_p_right, find_q_right = self.find_LCA(cur.right, p, q)
        find_p = find_p_left or find_p_right
        find_q = find_q_left or find_q_right
        if cur == p:
            find_p = True
        if cur == q:
            find_q = True
        if find_p and find_q:
            if not self.find:
                self.ans = cur
                self.find = True
            return True, True
        return find_p, find_q