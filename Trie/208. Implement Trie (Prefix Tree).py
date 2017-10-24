# Implement a trie with insert, search, and startsWith methods.

# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

# idea: each node can have 26 subnodes, whether we extend this tree depends on the new words
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
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.__find(prefix) != None
    
    def __find(self, word):
        tmp_node = self.root
        for char in word:
            tmp_node = tmp_node.next[ord(char) - ord('a')]
            if not tmp_node:
                break
        return tmp_node
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)