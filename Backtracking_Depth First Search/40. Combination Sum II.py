# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

# Solution 1:
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        used = [False for _ in range(len(candidates))]
        self.helper(candidates, target, res, 0, [], 0, used)
        return res

    def helper(self, candidates, target, res, idx, curRes, curSum, used):
        if idx == len(candidates):
            if curSum == target:
                res.append(curRes)
            return

        if curSum > target:
            return

        if idx > 0 and candidates[idx] == candidates[idx - 1] and not used[idx - 1]:
            self.helper(candidates, target, res, idx + 1, curRes, curSum, used)
        else:
            used[idx] = True
            self.helper(candidates, target, res, idx + 1, curRes + [candidates[idx]], curSum + candidates[idx], used)
            used[idx] = False
            self.helper(candidates, target, res, idx + 1, curRes, curSum, used)



# Solution 2:
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.helper(candidates, target, res, 0, [], 0)
        return res

    def helper(self, candidates, target, res, idx, curRes, curSum):
        if curSum == target:
            res.append(curRes)
            return

        if curSum > target:
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            self.helper(candidates, target, res, i + 1, curRes + [candidates[i]], curSum + candidates[i])
