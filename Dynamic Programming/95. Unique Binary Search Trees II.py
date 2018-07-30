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
        return self.helper(1, n, memo)
    
    def helper(self, l, r, memo):
        if l > r:
            return [None]
        if memo[l - 1][r - 1] != None:
            return memo[l - 1][r - 1]
        
        res = []
        for i in range(l, r + 1):
            leftSubTree = self.helper(l, i - 1, memo)
            rightSubTree = self.helper(i + 1, r, memo)
            for lNode in leftSubTree:
                for rNode in rightSubTree:
                    newNode = TreeNode(i)
                    newNode.left = lNode
                    newNode.right = rNode
                    res.append(newNode)
        memo[l - 1][r - 1] = res
        return res
