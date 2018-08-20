# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
#
# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:
#
# Note:
# The total number of elements of the given matrix will not exceed 10,000.

# idea: traverse the matrix by the first row and the last column

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        res = []
        rowNum, colNum = len(matrix), len(matrix[0])
        isUp = True
        for i in range(colNum):
            tmpRes = self.helper(0, i, matrix)
            if isUp:
                res.extend(tmpRes[::-1])
            else:
                res.extend(tmpRes)
            isUp = not isUp

        for i in range(1, rowNum):
            tmpRes = self.helper(i, colNum - 1, matrix)
            if isUp:
                res.extend(tmpRes[::-1])
            else:
                res.extend(tmpRes)
            isUp = not isUp
        return res

    def helper(self, row, col, matrix):
        tmpRes = [matrix[row][col]]
        while True:
            row += 1
            col -= 1
            if row < len(matrix) and col >= 0:
                tmpRes.append(matrix[row][col])
            else:
                break
        return tmpRes
