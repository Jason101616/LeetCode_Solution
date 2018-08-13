# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.findNSum(nums, 0, target, 4, res, [])
        return res

    def findNSum(self, nums, idx, target, N, res, curRes):
        if len(nums) - idx < N or N < 2:
            return

        if N == 2:
            l, r = idx, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append(curRes + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and l - 1 >= 0 and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and r + 1 < len(nums) and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:  # nums[l] + nums[r] > target
                    r -= 1
        else:
            for i in range(idx, len(nums) - N + 1):
                if target < nums[i] * N or target > nums[-1] * N:
                    break
                if i == idx or i > idx and nums[i - 1] != nums[i]:
                    self.findNSum(nums, i + 1, target - nums[i], N - 1, res, curRes + [nums[i]])
