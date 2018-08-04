# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

# Example:

# Given nums = [5, 2, 6, 1]

# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].

# binary search, with each node store the number of number smaller than current number
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.smaller = 0  # number of number smaller than current number
        self.left = None  # binary tree
        self.right = None


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [None for _ in range(len(nums))]
        root = None
        for i in range(len(nums) - 1, -1, -1):
            root = self.insert(root, nums[i], res, i, 0)
        return res

    def insert(self, root, val, res, index, pre_sum):
        if not root:
            root = TreeNode(val)
            res[index] = pre_sum
            return root
        if root.val > val:
            root.smaller += 1
            root.left = self.insert(root.left, val, res, index, pre_sum)
        else:  # root.val <= val
            plus = 0
            if root.val < val:
                plus = 1
            root.right = self.insert(root.right, val, res, index, pre_sum + root.smaller + plus)
        return root
