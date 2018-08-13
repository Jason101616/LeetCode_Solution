# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# binary search, time: O(logn), space: O(1)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        l, r, find = 0, len(nums) - 1, False
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                find = True
            if l == r:
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if not find:
            return [-1, -1]
        if nums[r] != target or r < 0:
            r += 1

        ll, rr = 0, len(nums) - 1
        while ll <= rr:
            if ll == rr:
                break
            mid = ll + (rr - ll) // 2
            if nums[mid] <= target:
                ll = mid + 1
            else:
                rr = mid
        if nums[rr] != target:
            rr -= 1
        return [r, rr]
