# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true, otherwise return false.
#
# Example 1:
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:
#
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.helper(nums, target, 0, len(nums) - 1)

    def helper(self, nums, target, left, right):
        # [2, 2, 2, 3, 4, 2]
        if left > right:
            return False
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True

        if nums[left] < nums[mid]:  # left side is normal
            # if target is in the left side, search on the left
            if nums[left] <= target < nums[mid]:
                return self.helper(nums, target, left, mid - 1)
            # else search on the right side
            else:
                return self.helper(nums, target, mid + 1, right)
        elif nums[mid] < nums[right]:  # right side is normal
            # if target is in the right side, search on the right side
            if nums[mid] < target <= nums[right]:
                return self.helper(nums, target, mid + 1, right)
            # else search on the left side
            else:
                return self.helper(nums, target, left, mid - 1)
        else:  # both side are not normal
            # first search on the left side
            res = self.helper(nums, target, left, mid - 1)
            # not find, search on the right side
            if not res:
                return self.helper(nums, target, mid + 1, right)
            # return ans
            else:
                return res
