# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Solution 1: top to bottom method
# (1) generate the node
# (2) use divide and conquer to wire those node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        self.node_list = []
        for num in nums:
            new_node = TreeNode(num)
            self.node_list.append(new_node)
        self.wire(0, len(self.node_list) - 1)
        return self.node_list[(len(self.node_list) - 1) // 2]

    def wire(self, left, right):
        if left == right:
            return
        cur_pos = (left + right) // 2
        cur_node = self.node_list[cur_pos]
        left_pos = (left + cur_pos - 1) // 2
        if left_pos >= left and left_pos != cur_pos:
            cur_node.left = self.node_list[left_pos]
            self.wire(left, cur_pos - 1)
        right_pos = (right + cur_pos + 1) // 2
        if right_pos != cur_pos:
            cur_node.right = self.node_list[right_pos]
            self.wire(cur_pos + 1, right)


# Solution 2: Find the root first, then recursively wire each left and right subtree. Button to top
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) // 2
        cur_node = TreeNode(nums[mid])
        cur_node.left = self.sortedArrayToBST(nums[:mid])
        cur_node.right = self.sortedArrayToBST(nums[mid + 1:])
        return cur_node
