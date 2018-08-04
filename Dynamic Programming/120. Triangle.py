# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


# Solution 1: DFS. TLE
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return 0
        self.triangle = triangle
        self.ans = []
        self.find_min(triangle[0][0], 1, 0)
        self.find_min(triangle[0][0], 1, 1)
        return min(self.ans)

    def find_min(self, prev_ans, cur_level, cur_index):
        if cur_level > len(self.triangle) - 1:
            self.ans.append(prev_ans)
            return
        cur_ans = prev_ans + self.triangle[cur_level][cur_index]
        self.find_min(cur_ans, cur_level + 1, cur_index)
        self.find_min(cur_ans, cur_level + 1, cur_index + 1)


# Solution 2: DP. update a new triangle
# new_tri[i][j] += min(new_tri[i - 1][j - 1], new_tri[i - 1][j])
# the edge case should be handled seperately
# the minimum number in the last row is the answer
from copy import deepcopy


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return 0
        new_tri = deepcopy(triangle)
        len_tri = len(triangle)
        for i in range(1, len_tri):
            new_tri[i][0] += new_tri[i - 1][0]
            new_tri[i][len(new_tri[i])
                       - 1] += new_tri[i - 1][len(new_tri[i - 1]) - 1]
            for j in range(1, len(new_tri[i]) - 1):
                new_tri[i][j] += min(new_tri[i - 1][j - 1], new_tri[i - 1][j])
        return min(new_tri[len_tri - 1])

# Solution 3: DP. buttom-up
# not easy to think. see http://www.cnblogs.com/grandyang/p/4286274.html
