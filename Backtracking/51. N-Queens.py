# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# For example,
# There exist two distinct solutions to the 4-queens puzzle:

# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

# backtracking
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        columns = [None for i in range(n)]
        self.find_ans(res, 0, columns, n)
        return self.draw_res(res, n)
    
    def find_ans(self, res, row, columns, n):
        # columns[r] = c indicates that row r has a queen at column c
        if row == n:
            res.append(copy.deepcopy(columns))
            return
        for col in range(n):
            if self.is_valid(columns, row, col):
                columns[row] = col
                self.find_ans(res, row + 1, columns, n)
    
    def is_valid(self, columns, row, col):
        for r in range(row):
            c = columns[r]
            if c == col:
                # previous row has a queen in the same column
                return False
			# Check diagonals: if the distance between the columns equals the distance
			# between the rows, then they’re in the same diagonal.
            col_dis = abs(c - col)
            row_dis = row - r
            if col_dis == row_dis:
                return False
        return True
    
    def draw_res(self, res, n):
        ret = []
        for re in res:
            ans = []
            for num in re:
                str_arr = []
                for i in range(n):
                    if i != num:
                        str_arr.append('.')
                    else:
                        str_arr.append('Q')
                cur_row = ''.join(str_arr)
                ans.append(cur_row)
            ret.append(ans)
        return ret