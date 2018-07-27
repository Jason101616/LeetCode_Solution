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
        row, col = len(board), len(board[0])
        visited = [[False for _ in range(col)] for __ in range(row)]
        for i in range(row):
            for j in range(col):
                if self.search_word(visited, i, j, word, board, 0):
                    return True
        return False
    
    def search_word(self, visited, i, j, word, board, index):
        if index == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[index]:
            return False
        visited[i][j] = True
        if self.search_word(visited, i + 1, j, word, board, index + 1):
            return True
        if self.search_word(visited, i - 1, j, word, board, index + 1):
            return True
        if self.search_word(visited, i, j + 1, word, board, index + 1):
            return True
        if self.search_word(visited, i, j - 1, word, board, index + 1):
            return True
        visited[i][j] = False
        return False
        