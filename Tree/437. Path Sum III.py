# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# idea: dfs + hash table count sum
# time: O(n)
# space: if balanced O(logn), worst case O(n)
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        sum_dict = collections.defaultdict(lambda: 0)
        self.res = 0
        self.find_path(sum_dict, None, root, sum)
        return self.res

    def find_path(self, sum_dict, cur_sum, cur_node, target):
        if not cur_node:
            return
        if not cur_sum:
            cur_sum = 0
        cur_sum += cur_node.val
        if cur_sum == target:
            self.res += 1
        self.res += sum_dict[cur_sum - target]
        sum_dict[cur_sum] += 1
        self.find_path(sum_dict, cur_sum, cur_node.left, target)
        self.find_path(sum_dict, cur_sum, cur_node.right, target)
        sum_dict[cur_sum] -= 1
