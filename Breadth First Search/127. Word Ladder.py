# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

# naive BFS solution, TLE
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
            
        self.wordDict = set(wordList)
        word_queue = deque()
        self.memo = set()
        length = 0
        word_queue.append(beginWord)
        self.memo.add(beginWord)
        while word_queue:
            length += 1
            size = len(word_queue)
            for i in range(size):
                cur_word = word_queue.popleft()
                if cur_word == endWord:
                    return length
                possible_next = self.find_next(cur_word)
                for word in possible_next:
                    word_queue.append(word)
                    self.memo.add(word)
        
        return 0
    
    def find_next(self, cur_word):
        def one_char_diff(word1, word2):
            if len(word1) != len(word2):
                return False
            diff_cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_cnt += 1
                if diff_cnt >= 2:
                    return False
            return True
        
        poss_list = []
        for word in self.wordDict:
            if word not in self.memo and one_char_diff(cur_word, word):
                poss_list.append(word)
        return poss_list
        

# BFS with proprocessing
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """ 
        wordDict = self.pre_process(wordList)
        word_queue = collections.deque()
        visited = set()
        length = 0
        word_queue.append(beginWord)
        visited.add(beginWord)
        while word_queue:
            length += 1
            size = len(word_queue)
            for i in range(size):
                cur_word = word_queue.popleft()
                if cur_word == endWord:
                    return length
                for i in range(len(cur_word)):
                    part_word = cur_word[:i] + '_' + cur_word[i + 1:]
                    neighword_words = wordDict[part_word]
                    for word in neighword_words:
                        if word not in visited:
                            visited.add(word)
                            word_queue.append(word)
        return 0

    def pre_process(self, word_list):
            word_dict = collections.defaultdict(lambda: [])
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i + 1:]
                    word_dict[s].append(word)
            return word_dict
        