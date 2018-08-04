# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Time:  O(m * n)
# Space: O(m * n)
# idea: very straightforward DP.
# it can be optimized, see: https://discuss.leetcode.com/topic/15265/0ms-5-lines-dp-solution-in-c-with-explanations
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[1 for _ in range(n)] for __ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[m - 1][n - 1]
