# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# idea: backtracing, same idea as 46, except that use a set to record whether a permutation has been added to the list

import copy
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret_list = []
        per_set = set()
        self.per(nums, ret_list, per_set, 0)
        return ret_list
            
    
    def per(self, nums, ret_list, per_set, begin):
        if begin >= len(nums):
            if tuple(nums) not in per_set:
                ret_list.append(copy.deepcopy(nums))
                per_set.add(tuple(nums))
            return
        
        for i in range(begin, len(nums)):
            if i != begin:
                nums[i], nums[begin] = nums[begin], nums[i]
            self.per(nums, ret_list, per_set, begin + 1)
            if i != begin:
                nums[i], nums[begin] = nums[begin], nums[i]