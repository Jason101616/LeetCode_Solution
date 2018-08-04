# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# Solution 1: use a set to delete the duplication. TLE.


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        self.target = target
        self.ans = set()
        self.candidates = sorted(candidates)
        self.candidates_len = len(candidates)
        self.find_ans([], 0, 0)

        self.ans = list(self.ans)
        for i in range(len(self.ans)):
            self.ans[i] = list(self.ans[i])
        return self.ans

    def find_ans(self, cur_list, cur_sum, index):
        if cur_sum == self.target:
            self.ans.add(tuple(deepcopy(cur_list)))
            return
        if cur_sum > self.target:
            return
        for i in range(index, self.candidates_len):
            cur_list.append(self.candidates[i])
            self.find_ans(cur_list, cur_sum + self.candidates[i], i + 1)
            cur_list.pop()


# Solution 2: add a Judgment statement in the for loop
from copy import deepcopy


class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if i > index and self.candidates[i] == self.candidates[i - 1]:
                continue
            cur_list.append(self.candidates[i])
            self.find_ans(cur_list, cur_sum + self.candidates[i], i + 1)
            cur_list.pop()
