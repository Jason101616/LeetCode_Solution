# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],w
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# backtracking, store whether each element has been used
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = [False for _ in range(len(nums))]
        res = []
        self.helper(nums, [], used, res)
        return res

    def helper(self, nums, curRes, used, res):
        if len(curRes) == len(nums):
            res.append(curRes)
            return

        for idx, num in enumerate(nums):
            if not used[idx]:
                used[idx] = True
                self.helper(nums, curRes + [num], used, res)
                used[idx] = False
