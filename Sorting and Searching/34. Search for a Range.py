# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

# idea: binary search
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        one_target_pos = self.find_target(nums, target)
        if one_target_pos == -1:
            return [-1, -1]
        left_pos = self.find_left(nums, one_target_pos)
        right_pos = self.find_right(nums, one_target_pos)
        return [left_pos, right_pos]

    def find_target(self, nums, target):
        # binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def find_left(self, nums, one_target_pos):
        l, r = 0, one_target_pos
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == nums[one_target_pos]:
                if mid == 0:
                    return mid
                elif nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    r = mid - 1
            elif nums[mid] < nums[one_target_pos]:
                l = mid + 1

    def find_right(self, nums, one_target_pos):
        l, r = one_target_pos, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == nums[one_target_pos]:
                if mid == len(nums) - 1:
                    return mid
                elif nums[mid] < nums[mid + 1]:
                    return mid
                else:
                    l = mid + 1
            elif nums[mid] > nums[one_target_pos]:
                r = mid - 1
