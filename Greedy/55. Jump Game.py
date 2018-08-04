# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false.

# Greedy
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0  # the longest points can be reached from current point
        for index, num in enumerate(nums):
            max_jump = max(max_jump - 1, num)
            if max_jump + index >= len(nums) - 1:
                return True
            if max_jump == 0:
                return False
