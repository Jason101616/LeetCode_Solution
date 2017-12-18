# Given two sparse matrices A and B, return the result of AB.

# You may assume that A's column number is equal to B's row number.

# Example:

# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]


#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |

# idea: 固定A的某一个数，一列列遍历用到A的这个数的B
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(A), len(B[0])
        ret_matrix = [[0 for _ in range(col)] for __ in range(row)]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    for k in range(col):
                        if B[j][k] != 0:
                            ret_matrix[i][k] += A[i][j] * B[j][k];
        return ret_matrix