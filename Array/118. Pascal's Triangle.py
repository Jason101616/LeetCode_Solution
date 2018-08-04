# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


# idea: handle the triangle row by row
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]
        row_0 = [1]
        row_1 = [1, 1]
        ans = [row_0, row_1]
        for i in range(3, numRows + 1):
            cur_ans = [None] * i
            cur_ans[0] = 1
            for j in range(1, i - 1):
                cur_ans[j] = ans[i - 2][j - 1] + ans[i - 2][j]
            cur_ans[i - 1] = 1
            ans.append(cur_ans)
        return ans
