# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        len_nums = len(nums)
        self.dp = [[0 for _ in range(len_nums)] for __ in range(len_nums)]
        for i in range(len_nums):
            self.dp[i][i] = nums[i]
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                self.dp[i][j] = self.dp[i][j - 1] + nums[j]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[i][j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)