# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

from copy import deepcopy


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.ans = []
        self.total_num = len(nums)
        self.find_ans([], 0, nums)
        return self.ans

    def find_ans(self, prev_ans, prev_num, nums):
        if prev_num == self.total_num:
            self.ans.append(deepcopy(prev_ans))
            return
        self.find_ans(prev_ans, prev_num + 1, nums)
        prev_ans.append(nums[prev_num])
        self.find_ans(prev_ans, prev_num + 1, nums)
        prev_ans.pop()


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.ans = []
        self.total_num = len(nums)
        self.find_ans([], 0, nums)
        return self.ans

    def find_ans(self, prev_ans, prev_num, nums):
        if prev_num == self.total_num:
            self.ans.append(prev_ans)
            return
        self.find_ans(prev_ans, prev_num + 1, nums)
        self.find_ans(prev_ans + [nums[prev_num]], prev_num + 1, nums)