# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique solution.
# The given board size is always 9x9.

from pprint import pprint

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        self.helper(board)

    def helper(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        if self.isValid(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if self.helper(board):
                                return True
                    board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, row, col, tmpAns):
        for i in range(9):
            if i != row and board[i][col] == tmpAns:
                return False
            if i != col and board[row][i] == tmpAns:
                return False
            tmpRow, tmpCol = 3 * (row // 3) + i // 3, 3 * (col // 3) + i % 3
            if tmpRow != row and tmpCol != col and board[tmpRow][tmpCol] != '.' and board[tmpRow][tmpCol] == tmpAns:
                return False;  # check 3*3 block
        return True


if __name__ == '__main__':
    rawBoard = [
            ". 5 . . . . . . .",
            "9 6 . 5 3 . 2 7 .",
            ". 2 4 . . . . 6 .",
            ". . . . 1 5 9 . .",
            ". . . 8 . 7 . . .",
            ". . 7 4 2 . . . .",
            ". 8 . . . . 7 9 .",
            ". 4 1 . 5 9 . 3 6",
            ". . . . . . . 1 ."
    ]
    board = []
    for row in rawBoard:
        board.append(row.split())
    sol = Solution()
    sol.solveSudoku(board)
    pprint(board)
