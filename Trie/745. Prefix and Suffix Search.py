# Given many words, words[i] has weight i.

# Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

# Examples:
# Input:
# WordFilter(["apple"])
# WordFilter.f("a", "e") // returns 0
# WordFilter.f("b", "") // returns -1
# Note:
# words has length in range [1, 15000].
# For each test case, up to words.length queries WordFilter.f may be made.
# words[i] has length in range [1, 10].
# prefix, suffix have lengths in range [0, 10].
# words[i] and prefix, suffix queries consist of lowercase letters only.

# Solution 1: Brute force
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.pre_suf_dict = {}
        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                prefix = word[:i]
                for j in range(len(word) + 1):
                    suffix = word[j:]
                    self.pre_suf_dict[prefix + '#' + suffix] = index

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.pre_suf_dict[prefix + '#' + suffix] if (prefix + '#' + suffix) in self.pre_suf_dict else -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
