# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# idea: backtracing
import copy
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret_list = []
        self.per(nums, ret_list, 0)
        return ret_list
        
    
    def per(self, nums, ret_list, index):
        if index >= len(nums):
            ret_list.append(copy.deepcopy(nums))
            return
        
        for i in range(index, len(nums)):
            if i != index:
                self.swap(nums, index, i)
            self.per(nums, ret_list, index + 1)
            if i != index:
                self.swap(nums, index, i)
    
    def swap(self, nums, i1, i2):
        tmp = nums[i1]
        nums[i1] = nums[i2]
        nums[i2] = tmp
        
            
        