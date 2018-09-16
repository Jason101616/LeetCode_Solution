# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i to val.
#
# Example:
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
#
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.

# segment tree:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = 0


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, nums, left, right):
        if left > right:
            return None
        node = SegmentTreeNode(left, right)
        if left == right:
            node.sum = nums[left]
        else:
            mid = left + (right - left) // 2
            node.left = self.buildTree(nums, left, mid)
            node.right = self.buildTree(nums, mid + 1, right)
            if node.left:
                node.sum += node.left.sum
            if node.right:
                node.sum += node.right.sum
        return node

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

        def updateHelper(node, i, val):
            if node.start == node.end == i:
                node.sum = val
                return
            mid = node.start + (node.end - node.start) // 2
            if i <= mid:
                updateHelper(node.left, i, val)
            else:
                updateHelper(node.right, i, val)
            node.sum = node.left.sum + node.right.sum

        updateHelper(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        def sumRangeHelper(node, l, r):
            if node.start == l and node.end == r:
                return node.sum
            mid = node.start + (node.end - node.start) // 2
            if r <= mid:
                return sumRangeHelper(node.left, l, r)
            elif l > mid:
                return sumRangeHelper(node.right, l, r)
            else:
                return sumRangeHelper(node.left, l, mid) + sumRangeHelper(node.right, mid + 1, r)

        return sumRangeHelper(self.root, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


# binary indexed tree:
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.BIT = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            self.updateBIT(i, nums[i - 1])

    def updateBIT(self, idx, val):
        while idx < len(self.BIT):
            self.BIT[idx] += val
            idx += (idx & -idx)

    def readBIT(self, idx):
        res = 0
        while idx > 0:
            res += self.BIT[idx]
            idx -= (idx & -idx)
        return res

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.updateBIT(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.readBIT(j + 1) - self.readBIT(i)
