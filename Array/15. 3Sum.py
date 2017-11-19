# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


# idea: sort and it is another version of two sum, use set to remove duplication
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i
        ans = set()
        len_nums = len(nums)
        for i, num in enumerate(nums):
            target = -num
            for j in range(i + 1, len_nums):
                if target - nums[j] in nums_dict and nums_dict[target
                                                               - nums[j]] > j:
                    ans.add((nums[i], nums[j], nums[nums_dict[target
                                                              - nums[j]]]))
        ans = list(ans)
        for i, an in enumerate(ans):
            ans[i] = list(an)
        return ans