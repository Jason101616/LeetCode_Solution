# Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .
#
# Example:
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# Note:
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        self.dfs(res, (), nums, 0)
        return [list(ans) for ans in res]

    def dfs(self, res, curRes, nums, idx):
        if len(curRes) >= 2:
            res.add(curRes)

        for i in range(idx, len(nums)):
            if not curRes or nums[i] >= curRes[-1]:
                self.dfs(res, curRes + (nums[i],), nums, i + 1)
