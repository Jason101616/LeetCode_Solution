# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Write a function to determine if a given target is in the array.

# The array may contain duplicates.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.search_rotate(nums, target, 0, len(nums) - 1)
    
    def search_rotate(self, nums, target, left, right):
        # [2, 2, 2, 3, 4, 2]
        if left > right:
            return False
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        
        if nums[left] < nums[mid]:  # left side is normal
            # if target is in the left side, search on the left
            if target < nums[mid] and target >= nums[left]:
                return self.search_rotate(nums, target, left, mid - 1)
            # else search on the right side
            else:
                return self.search_rotate(nums, target, mid + 1, right)
        elif nums[mid] < nums[right]:   # right side is normal
            # if target is in the right side, search on the right side
            if target > nums[mid] and target <= nums[right]:
                return self.search_rotate(nums, target, mid + 1, right)
            # else search on the left side
            else:
                return self.search_rotate(nums, target, left, mid - 1)
        else:   # both side are not normal
            # first search on the left side
            res = self.search_rotate(nums, target, left, mid - 1)
            # not find, search on the right side
            if not res:
                return self.search_rotate(nums, target, mid + 1, right)
            # return ans
            else:
                return res
        