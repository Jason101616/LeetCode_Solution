# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.


# idea: from each coordinate use dfs
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        self.find = False
        self.board = board
        self.word = word
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                visited = set()
                self.find_path(0, i, j, visited)
        return self.find

    def find_path(self, index_word, row, col, visited):
        if index_word >= len(
                self.word) or self.word[index_word] != self.board[row][col]:
            return
        if index_word == len(
                self.word
        ) - 1 and self.word[index_word] == self.board[row][col]:
            self.find = True
            return
        visited.add((row, col))
        for i, j in self.can_visit_next(row, col, visited):
            self.find_path(index_word + 1, i, j, visited)
        visited.remove((row, col))

    def can_visit_next(self, row, col, visited):
        can_visit = []
        if row - 1 >= 0 and (row - 1, col) not in visited:
            can_visit.append((row - 1, col))
        if row + 1 <= len(self.board) - 1 and (row + 1, col) not in visited:
            can_visit.append((row + 1, col))
        if col - 1 >= 0 and (row, col - 1) not in visited:
            can_visit.append((row, col - 1))
        if col + 1 <= len(self.board[0]) - 1 and (row, col + 1) not in visited:
            can_visit.append((row, col + 1))
        return can_visit