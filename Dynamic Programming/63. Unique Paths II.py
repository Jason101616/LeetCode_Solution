# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100.


# Time:  O(m * n)
# Space: O(m * n)
# idea: Add a new row and col to handle edge case of Unique Path.
# It can be optimized, see https://discuss.leetcode.com/topic/15267/4ms-o-n-dp-solution-in-c-with-explanations

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0 for _ in range(col + 1)] for __ in range(row + 1)]
        memo[0][1] = 1

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if not obstacleGrid[i - 1][j - 1]:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[row][col]
