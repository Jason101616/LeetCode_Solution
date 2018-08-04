# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        # find from right, the first element smaller than its right element. mark the pos
        # if pos < 0, rearrange it as the lowest possible order 
        pos = len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pos = i
                break
        if pos == len(nums):
            nums.sort()
            return
        # start from pos to right, find the pos2, which satisfy nums[pos2] > nums[pos] >= nums[pos2+1]
        pos2 = len(nums) - 1
        for i in range(pos + 1, len(nums) - 1):
            if nums[i] > nums[pos] and nums[pos] >= nums[i + 1]:
                pos2 = i
                break
        # swap element in pos and pos2
        nums[pos], nums[pos2] = nums[pos2], nums[pos]
        # reverse the number start from pos+1
        nums[pos + 1:] = sorted(nums[pos + 1:])
        return
