# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# idea: same idea as 46, except need sort first and add two lines to delete duplicate.
# key point is that when want to use a number, and its value is the same as the previous number, this number can only be used when the previous number  have been used
# 先判断前面的一个数是否和自己相等，相等的时候则前面的数必须使用了，自己才能使用
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = []
        cur = []
        used = [False for _ in range(len(nums))]
        self.find_permutation(res, cur, nums, used)
        return res

    def find_permutation(self, res, cur, nums, used):
        if len(cur) == len(nums):
            res.append(list(cur))
            return
        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                cur.append(nums[i])
                used[i] = True
                self.find_permutation(res, cur, nums, used)
                used[i] = False
                cur.pop()