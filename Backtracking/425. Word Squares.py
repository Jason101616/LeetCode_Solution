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


# Solution 1: DFS + use a trie to prune.
class TrieNode:
    def __init__(self, is_word=False):
        self.next = {}
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
        cur_node = self.root
        for char in word:
            if char not in cur_node.next:
                cur_node.next[char] = TrieNode()
            cur_node = cur_node.next[char]
        cur_node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        end_node = self.__find_node(word)
        if end_node and end_node.is_word:
            return True
        return False

    def find_words(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.next:
                return []
            cur_node = cur_node.next[char]
        ans = []
        if cur_node.is_word:
            ans.append(prefix)
        for key in cur_node.next.keys():
            self.dfs(prefix + key, cur_node.next[key], ans)
        return ans

    def dfs(self, prefix, cur_node, ans):
        if cur_node.is_word:
            ans.append(prefix)
        for key in cur_node.next.keys():
            self.dfs(prefix + key, cur_node.next[key], ans)

    def __find_node(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.next:
                return None
            cur_node = cur_node.next[char]
        return cur_node


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
                ans.append(matrix[:])  # this is actually copy the matrix
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
