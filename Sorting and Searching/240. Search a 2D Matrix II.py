# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.

# Given target = 20, return false.

# Approach 1:
# 2-d binary search
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        return self.search(matrix, target, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)

    def search(self, matrix, target, r_left, r_right, c_left, c_right):
        if r_left > r_right or c_left > c_right:
            return False
        r_mid = r_left + (r_right - r_left) // 2
        c_mid = c_left + (c_right - c_left) // 2
        if matrix[r_mid][c_mid] == target:
            return True
        if matrix[r_mid][c_mid] < target:
            # the answer cannot be in the left up corner of the current matrix
            return self.search(matrix, target, r_left, r_right, c_mid + 1, c_right) or self.search(matrix, target,
                                                                                                   r_mid + 1, r_right,
                                                                                                   c_left, c_mid)
        else:
            # the answer cannot be in the right botton corner of the current matrix
            return self.search(matrix, target, r_left, r_right, c_left, c_mid - 1) or self.search(matrix, target,
                                                                                                  r_left, r_mid - 1,
                                                                                                  c_mid, c_right)


# Approach 2: 
# time: O(n + m)
class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False
