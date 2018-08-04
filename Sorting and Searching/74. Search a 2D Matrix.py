# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

# two nested binary search
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = self.find_row(matrix, target, 0, len(matrix) - 1)
        if row < 0:
            return False
        return self.find_element(matrix[row], target, 0, len(matrix[row]) - 1)

    def find_row(self, matrix, target, left, right):
        while right >= left:
            mid = left + (right - left) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return mid
            if target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def find_element(self, nums, target, left, right):
        while right >= left:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return True
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False
