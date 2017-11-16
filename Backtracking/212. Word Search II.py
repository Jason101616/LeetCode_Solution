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
        self.num_of_char = 26
        self.next = [None for _ in range(self.num_of_char)]
        self.is_word = is_word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur_node = self.root
        for char in word:
            if not cur_node.next[ord(char) - ord('a')]:
                cur_node.next[ord(char) - ord('a')] = TrieNode()
            cur_node = cur_node.next[ord(char) - ord('a')]
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
            cur_node = cur_node.next[ord(char) - ord('a')]
            if not cur_node:
                break
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
        for i in range(row):
            for j in range(col):
                visited = set()
                self.find_path(i, j, visited, board[i][j])
        return self.ans

    def find_path(self, row, col, visited, cur_string):
        if not self.trie.start_with(cur_string):
            return
        if self.trie.search(cur_string) and cur_string not in self.ans:
            self.ans.append(cur_string)
        visited.add((row, col))
        can_visit_next = self.can_visit_next(row, col, visited)
        for i, j in can_visit_next:
            self.find_path(i, j, visited, cur_string + self.board[i][j])
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