# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

# idea: use backtacking, but need to prune some repetitive results
# subsets([1,2,3,4]) = []
#                      // push(1)
#                      [1, subsets([2,3,4])] // if push N times in subsets([2,3,4]), the pop times is also N, so vec is also [1] after backtrack.
#                      // pop(), push(2)
#                      [2, subsets([3,4])]
#                      // pop(), push(3)
#                      [3, subsets([4])]
#                      // pop(), push(4)
#                      [4, subsets([])]
#                      // pop()
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.find_subsets(nums, 0, res, [])
        return res

    def find_subsets(self, nums, start, res, cur_res):
        res.append(cur_res)
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[i - 1]:
                self.find_subsets(nums, i + 1, res, cur_res + [nums[i]])
