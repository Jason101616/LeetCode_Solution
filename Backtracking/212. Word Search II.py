# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# For example,
# Given words = ["oath","pea","eat","rain"] and board =

# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.


# idea: same idea as Word Search I, but use Trie to stop backtracking earlier
class TrieNode:
    def __init__(self, is_word=False):
        self.next = {}
        self.is_word = is_word

        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.next:
                cur_node.next[char] = TrieNode()
            cur_node = cur_node.next[char]
        cur_node.is_word = True

    def start_with(self, prefix):
        return self.__find_node(prefix) != None

    def search(self, word):
        end_node = self.__find_node(word)
        if end_node and end_node.is_word:
            return True
        return False

    def __find_node(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.next:
                return None
            cur_node = cur_node.next[char]
        return cur_node


class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return False
        self.board = board
        # construct the trie
        self.trie = Trie()
        for word in words:
            self.trie.add(word)
        # use dfs to find the answer
        self.ans = []
        row = len(board)
        col = len(board[0])
        visited = [[False for _ in range(len(board[0]))] for __ in range(len(board))]
        for i in range(row):
            for j in range(col):
                self.find_path(i, j, visited, '')
        return self.ans

    def find_path(self, row, col, visited, cur_string):
        if self.trie.search(cur_string) and cur_string not in self.ans:
            self.ans.append(cur_string)
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]) or visited[row][col] or not self.trie.start_with(cur_string):
            return
        visited[row][col] = True
        self.find_path(row + 1, col, visited, cur_string + self.board[row][col])
        self.find_path(row - 1, col, visited, cur_string + self.board[row][col])
        self.find_path(row, col + 1, visited, cur_string + self.board[row][col])
        self.find_path(row, col - 1, visited, cur_string + self.board[row][col])
        visited[row][col] = False