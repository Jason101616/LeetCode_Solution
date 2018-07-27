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


# idea: same idea as Word Search I, but use Trie to stop backtracking earlier.
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.next = {}

        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curNode = self.root
        for char in word:
            if char not in curNode.next:
                curNode.next[char] = TrieNode()
            curNode = curNode.next[char]
        curNode.isWord = True

    def startWith(self, prefix):
        node = self.traverseHelper(prefix)
        return node != None

    def isInTrie(self, word):
        node = self.traverseHelper(word)
        return node != None and node.isWord

    def traverseHelper(self, word):
        curNode = self.root
        for char in word:
            if char not in curNode.next:
                return None
            curNode = curNode.next[char]
        return curNode


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        trie = Trie()
        for word in words:
            trie.insert(word)
        row, col = len(board), len(board[0])
        res = set()
        visited = [[False for _ in range(col)] for __ in range(row)]
        for i in range(row):
            for j in range(col):
                visited[i][j] = True
                self.searchWords(i, j, trie, board, res, visited, board[i][j])
                visited[i][j] = False
        return list(res)

    def searchWords(self, i, j, trie, board, res, visited, curRes):
        if not trie.startWith(curRes):
            return
        if trie.isInTrie(curRes):
            res.add(curRes)
        if i - 1 >= 0 and not visited[i - 1][j]:
            visited[i - 1][j] = True
            self.searchWords(i - 1, j, trie, board, res, visited, curRes + board[i - 1][j])
            visited[i - 1][j] = False
        if i + 1 < len(board) and not visited[i + 1][j]:
            visited[i + 1][j] = True
            self.searchWords(i + 1, j, trie, board, res, visited, curRes + board[i + 1][j])
            visited[i + 1][j] = False
        if j - 1 >= 0 and not visited[i][j - 1]:
            visited[i][j - 1] = True
            self.searchWords(i, j - 1, trie, board, res, visited, curRes + board[i][j - 1])
            visited[i][j - 1] = False
        if j + 1 < len(board[0]) and not visited[i][j + 1]:
            visited[i][j + 1] = True
            self.searchWords(i, j + 1, trie, board, res, visited, curRes + board[i][j + 1])
            visited[i][j + 1] = False