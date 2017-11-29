# Given a set of words (without duplicates), find all word squares you can build from them.

# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

# b a l l
# a r e a
# l e a d
# l a d y
# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:

# Input:
# ["area","lead","wall","lady","ball"]

# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Example 2:

# Input:
# ["abat","baba","atan","atal"]

# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).


# Solution 1: DFS + use a trie to prune. TLE...
class TrieNode:
    def __init__(self, is_word=False):
        self.num_of_char = 26
        self.next = [None] * self.num_of_char
        self.is_word = is_word


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        tmp_node = self.root
        for char in word:
            if not tmp_node.next[ord(char) - ord('a')]:
                tmp_node.next[ord(char) - ord('a')] = TrieNode()
            tmp_node = tmp_node.next[ord(char) - ord('a')]
        tmp_node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        end_node = self.__find(word)
        if end_node and end_node.is_word:
            return True
        return False

    def find_words(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tmp_node = self.root
        for char in prefix:
            tmp_node = tmp_node.next[ord(char) - ord('a')]
            if not tmp_node:
                return []
        self.ans = []
        if tmp_node.is_word:
            self.ans.append(prefix)
        for i in range(len(tmp_node.next)):
            if tmp_node.next[i] != None:
                self.dfs(prefix + chr(ord('a') + i), tmp_node.next[i])
        return self.ans

    def dfs(self, prefix, cur_node):
        if cur_node.is_word:
            self.ans.append(prefix)
        for i in range(len(cur_node.next)):
            if cur_node.next[i] != None:
                self.dfs(prefix + chr(ord('a') + i), cur_node.next[i])

    def __find(self, word):
        tmp_node = self.root
        for char in word:
            tmp_node = tmp_node.next[ord(char) - ord('a')]
            if not tmp_node:
                break
        return tmp_node


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words or not words[0]:
            return []
        matrix = []
        ans = []
        m = len(words)
        n = len(words[0]) if m else 0
        trie = Trie()
        for word in words:
            trie.insert(word)

        def search(word, line):
            matrix.append(word)
            if line == n:
                ans.append(matrix[:])
            else:
                prefix = ''.join(matrix[x][line] for x in range(line))
                for word in trie.find_words(prefix):
                    search(word, line + 1)
            matrix.pop()

        for word in words:
            search(word, 1)
        return ans


# Solution 2: use a dict to store all the prefix
import collections


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        m = len(words)
        n = len(words[0]) if m else 0
        mdict = collections.defaultdict(set)
        for word in words:
            for i in range(n):
                mdict[word[:i]].add(word)
        matrix = []
        ans = []

        def search(word, line):
            matrix.append(word)
            if line == n:
                ans.append(matrix[:])
            else:
                prefix = ''.join(matrix[x][line] for x in range(line))
                for word in mdict[prefix]:
                    search(word, line + 1)
            matrix.pop()

        for word in words:
            search(word, 1)
        return ans