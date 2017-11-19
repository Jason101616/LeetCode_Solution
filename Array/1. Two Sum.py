# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# idea: use a dictionary to record each element's value and position
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        len_nums = len(nums)
        for i in range(len_nums):
            if target - nums[i] in nums_dict and nums_dict[target
                                                           - nums[i]] != i:
                return [i, nums_dict[target - nums[i]]]
            nums_dict[nums[i]] = i
