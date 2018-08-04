# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]

# idea: use backtracking
from copy import deepcopy


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        self.target = target
        self.ans = []
        self.candidates = sorted(candidates)
        self.candidates_len = len(candidates)
        self.find_ans([], 0, 0)
        return self.ans

    def find_ans(self, cur_list, cur_sum, index):
        if cur_sum == self.target:
            self.ans.append(deepcopy(cur_list))
            return
        if cur_sum > self.target:
            return
        for i in range(index, self.candidates_len):
            cur_list.append(self.candidates[i])
            self.find_ans(cur_list, cur_sum + self.candidates[i], i)
            cur_list.pop()
