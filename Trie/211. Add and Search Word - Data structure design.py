# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# For example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.

# idea: the same idea as 208. Implement Trie (Prefix Tree). Except that, for search, using backtracing.
class TrieNode:
    def __init__(self, is_word=False):
        self.num_of_char = 26
        self.next = [None] * self.num_of_char
        self.is_word = is_word
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.__search_from_node(word, self.root)
    
    def __search_from_node(self, string, node):
        if not node:
            return False
        
        tmp_node = node
        for i in range(len(string)):
            if string[i] != '.':
                tmp_node = tmp_node.next[ord(string[i]) - ord('a')]
                if not tmp_node:
                    break
            else:
                for nxt in tmp_node.next:
                    if self.__search_from_node(string[i+1:], nxt):
                        return True
                return False
                    
        return bool(tmp_node and tmp_node.is_word)
                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)