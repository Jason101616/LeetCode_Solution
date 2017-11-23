# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# For example, given the following matrix:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.


# idea: the transition function is: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[None for _ in range(col)] for __ in range(row)]
        for i in range(col):
            dp[0][i] = int(matrix[0][i])
        for i in range(row):
            dp[i][0] = int(matrix[i][0])
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i - 1][j],
                               dp[i][j - 1], dp[i - 1][j - 1]) + 1 if int(
                                   matrix[i][j]) == 1 else 0
        ans = 0
        for i in range(row):
            ans = max(ans, max(dp[i]))
        return ans * ans
