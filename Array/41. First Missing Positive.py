# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.

# put each element to where it should be, then scan from the left, the first element violate the principle is the answer
# where it should be is defined as nums[i] should be placed at nums[nums[i] - 1] if nums[i] < len(nums)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[tmp - 1] = tmp
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i] # be careful!!! this kind of swap will lead to bug

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
