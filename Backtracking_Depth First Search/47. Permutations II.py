# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# idea: same idea as 46, except need sort first and add two lines of code to delete duplicate.
# key point is that when want to use a number, and its value is the same as the previous number,
# this number can only be used when the previous number have been used.
# 先判断前面的一个数是否和自己相等，相等的时候则前面的数必须使用了，自己才能使用
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        used = [False for _ in range(len(nums))]
        nums.sort()
        self.helper(nums, res, used, [])
        return res

    def helper(self, nums, res, used, curRes):
        if len(nums) == len(curRes):
            res.append(curRes)
            return

        for idx, num in enumerate(nums):
            if not used[idx]:
                if idx > 0 and nums[idx] == nums[idx - 1] and not used[idx - 1]:
                    continue
                used[idx] = True
                self.helper(nums, res, used, curRes + [num])
                used[idx] = False
