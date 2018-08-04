# CtCI P188 17.13
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
        Returns if the word is in the trie. Not a prefix.
        :type word: str
        :rtype: bool
        """
        end_node = self.__find_node(word)
        if end_node and end_node.is_word:
            return True
        return False

    def start_with(self, prefix):
        """
        Return True if at least one word in the Trie start with the given prefix.
        Else return False
        :param prefix: str
        :return: bool
        """
        return self.__find_node(prefix) != None

    def find_words(self, prefix):
        """
        Returns all the words in the trie that starts with the given prefix.
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
            self.__dfs(prefix + key, cur_node.next[key], ans)
        return ans

    def __dfs(self, prefix, cur_node, ans):
        if cur_node.is_word:
            ans.append(prefix)
        for key in cur_node.next.keys():
            self.__dfs(prefix + key, cur_node.next[key], ans)

    def __find_node(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.next:
                return None
            cur_node = cur_node.next[char]
        return cur_node


def respace(string, string_list):
    my_trie = Trie()
    for str in string_list:
        my_trie.insert(str)
    memo = {}
    return find_ans(string, set(string_list), my_trie, memo)


def find_ans(string, string_set, my_trie, memo):
    if not string or string in string_set:
        memo[string] = 0
        return 0
    if string in memo:
        return memo[string]

    res = len(string)
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if not my_trie.start_with(string[i:j]):
                break
            if string[i:j] in string_set:
                res = min(res, i + find_ans(string[j:], string_set, my_trie, memo))
    memo[string] = res
    return memo[string]
