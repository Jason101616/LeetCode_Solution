# This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

# idea: first use hash table, then use two pointers

class WordDistance(object):
    
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.word_dict = collections.defaultdict(lambda: [])
        for index, word in enumerate(words):
            self.word_dict[word].append(index)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos_1, pos_2 = self.word_dict[word1], self.word_dict[word2]
        index1 = index2 = 0
        min_dis = float('inf')
        while index1 < len(pos_1) and index2 < len(pos_2):
            min_dis = min(min_dis, abs(pos_1[index1] - pos_2[index2]))
            if pos_1[index1] < pos_2[index2]:
                index1 += 1
            else:
                index2 += 1
        return min_dis
                
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)