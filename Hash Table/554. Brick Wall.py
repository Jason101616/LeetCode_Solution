# There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

# The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

# If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

# You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

# Example:
# Input:
# [[1,2,2,1],
#  [3,1,2],
#  [1,3,2],
#  [2,4],
#  [3,1,2],
#  [1,3,1,1]]
# Output: 2
# Explanation:

# Note:
# The width sum of bricks in different rows are the same and won't exceed INT_MAX.
# The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.

# idea: make use of a HashMap which is used to store entries in the form: (sum, count). Here, sum refers to the cumulative sum of the bricks' widths encountered in the current row, and count refers to the number of times the corresponding sum is obtained. Traverse every layer and build the hashmap. Then the maximum value in the hashmap can be used to compute the answer.
# Time complexity : O(n). We traverse over the complete bricks only once. n is the total number of bricks in a wall.
# Space complexity : O(m). map will contain atmost m entries, where m refers to the width of the wall.
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        cntDict = collections.defaultdict(lambda: 0)
        for layer in wall:
            curSum = 0
            for i in range(len(layer) - 1):
                curSum += layer[i]
                cntDict[curSum] += 1
        return len(wall) - max(cntDict.values()) if len(cntDict) else len(wall)
