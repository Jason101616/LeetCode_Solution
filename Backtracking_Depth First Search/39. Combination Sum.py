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

# idea: backtracking
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(candidates, target, 0, [], res, 0)
        return res

    def helper(self, candidates, target, curSum, curRes, res, idx):
        if curSum > target:
            return

        if curSum == target:
            res.append(curRes)
            return

        for i in range(idx, len(candidates)):
            self.helper(candidates, target, curSum + candidates[i], curRes + [candidates[i]], res, i)
