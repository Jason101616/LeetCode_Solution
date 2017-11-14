# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Example 1:
#      3
#     / \
#    2   3
#     \   \
#      3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
# Maximum amount of money the thief can rob = 4 + 5 = 9.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# idea: when ask the best value of one node, we should know 7 things.
# 1. its own value; 2. its left child's value; 3. its right child's value
# 4. its left child's left child's value; 5. its left child's right child's value;
# 6. its right child's left child's value; 7. its right child's right child's value
# the best value of current node is either: 1 + 4 + 5 + 6 + 7 or 2 + 3
# compare them and return current node's best value and its left child's value and its right child's value to its parent
# because its parent need those information
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max = 0
        self.rob_tree(root)
        return self.max

    def rob_tree(self, node):
        if not node:
            return 0, 0, 0
        l_son, l_grandson_l, l_grandson_r = self.rob_tree(node.left)
        r_son, r_grandson_l, r_grandson_r = self.rob_tree(node.right)
        cur_max = max(node.val + l_grandson_l + l_grandson_r + r_grandson_l +
                      r_grandson_r, l_son + r_son)
        if cur_max > self.max:
            self.max = cur_max
        return cur_max, l_son, r_son
