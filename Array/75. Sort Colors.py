# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.

# click to show follow up.

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

# Could you come up with an one-pass algorithm using only constant space?

# use two pointers to indicate the boarderline of 0 and 2.
# scan the nums, if current the number is 0 than swap it to left, if it is 1 than not move this number, if it is 2 than swap it to right
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        li, ri = 0, len(nums) - 1
        i = 0
        while i <= ri:
            if nums[i] == 0:
                if i != li:
                    nums[li], nums[i] = nums[i], nums[li]
                i += 1
                li += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[ri], nums[i] = nums[i], nums[ri]
                ri -= 1

# k color solution. Fix the color one by one. Time: O(kn)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, end, k = 0, len(nums) - 1, 3  # k is the number of color
        for i in range(k):
            start = self.helper(nums, start, end, i)

    def helper(self, nums, start, end, color):
        while start < end:
            while start < end and nums[start] == color:
                start += 1
            while start < end and nums[end] != color:
                end -= 1
            nums[start], nums[end] = nums[end], nums[start]
        return start
