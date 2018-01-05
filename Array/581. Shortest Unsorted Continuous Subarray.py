# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

# idea: find the sorted array in the beginning and end first, then enlarge the middle point. Be careful about the edge case.
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin_index = self.find_begin_asc(nums)
        if begin_index == len(nums) - 1:
            return 0
        end_index = self.find_end_asc(nums)
        min_val, max_val = self.check_middle(nums, begin_index, end_index)
        while begin_index >= 0:
            if nums[begin_index] <= min_val:
                break
            begin_index -= 1
        while end_index <= len(nums) - 1:
            if nums[end_index] >= max_val:
                break
            end_index += 1

        return end_index - begin_index - 1

    def find_begin_asc(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i + 1]:
                break
            i += 1
        return i

    def find_end_asc(self, nums):
        i = len(nums) - 1
        while i > 0:
            if nums[i] < nums[i - 1]:
                break
            i -= 1
        return i

    def check_middle(self, nums, left, right):
        min_val, max_val = float('inf'), float('-inf')
        for i in range(left, right + 1):
            if nums[i] > max_val:
                max_val = nums[i]
            if nums[i] < min_val:
                min_val = nums[i]
        return min_val, max_val
