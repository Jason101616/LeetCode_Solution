# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# idea: use recursion. pick one node as the root, and divide the tree into left subtree and right subtree. Then combine all the possible combination. Also define a memo to store the calculated outcome to accelerate the implementation.


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        memo = [[None for _ in range(n)] for __ in range(n)]
        return self.genTrees(1, n, memo)

    def genTrees(self, left, right, memo):
        if left > right:
            return [None]

        if memo[left - 1][right - 1] != None:
            return memo[left - 1][right - 1]
        ret_list = []
        for i in range(left, right + 1):
            left_subtree = self.genTrees(left, i - 1, memo)
            right_subtree = self.genTrees(i + 1, right, memo)
            for j in range(len(left_subtree)):
                for k in range(len(right_subtree)):
                    new_node = TreeNode(i)
                    new_node.left = left_subtree[j]
                    new_node.right = right_subtree[k]
                    ret_list.append(new_node)
        return ret_list
