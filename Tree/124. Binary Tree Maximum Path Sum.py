# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42



# idea: DFS search or backtracing
# naive implementation
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return 0
        leftSum = self.helper(node.left)
        rightSum = self.helper(node.right)
        curRes = node.val
        if leftSum > 0:
            curRes += leftSum
        if rightSum > 0:
            curRes += rightSum
        if curRes > self.res:
            self.res = curRes
        retRes = max(node.val, node.val + max(leftSum, rightSum))
        if retRes > self.res:
            self.res = retRes
        return retRes

# better version
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return 0
        leftSum = max(self.helper(node.left), 0)
        rightSum = max(self.helper(node.right), 0)
        if leftSum + rightSum + node.val > self.res:
            self.res = leftSum + rightSum + node.val
        return max(leftSum, rightSum) + node.val
