# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        res = self.search_rotate(nums, target, 0, len(nums) - 1)
        return res if res is not False else -1
    
    def search_rotate(self, nums, target, left, right):
        # [2, 2, 2, 3, 4, 2]
        if left > right:
            return False
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        
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
            if res is False:
                return self.search_rotate(nums, target, mid + 1, right)
            # return ans
            else:
                return res
        