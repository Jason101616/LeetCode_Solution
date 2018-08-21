# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        columns = [None for i in range(n)]
        self.find_ans(0, columns, n)
        return self.res

    def find_ans(self, row, columns, n):
        # columns[r] = c indicates that row r has a queen at column c
        if row == n:
            self.res += 1
            return
        for col in range(n):
            if self.is_valid(columns, row, col):
                columns[row] = col
                self.find_ans(row + 1, columns, n)

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
