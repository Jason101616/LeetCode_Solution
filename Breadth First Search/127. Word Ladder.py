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


# Bi-direction BFS
from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordDict = self.preProcess(wordList)
        beginQ, endQ = deque([beginWord]), deque([endWord])
        beginVisited, endVisited = {beginWord}, {endWord}
        step = 1
        while beginQ or endQ:
            if beginVisited & endVisited:
                return step
            step += 1
            if 0 < len(beginQ) <= len(endQ):
                self.queueHelper(beginQ, beginVisited, wordDict)
            else:
                self.queueHelper(endQ, endVisited, wordDict)
        return 0

    def queueHelper(self, q, visited, wordDict):
        curLen = len(q)
        for i in range(curLen):
            curWord = q.popleft()
            for i in range(len(curWord)):
                nextWords = wordDict[curWord[:i] + '_' + curWord[i + 1:]]
                for word in nextWords:
                    if word not in visited:
                        visited.add(word)
                        q.append(word)

    def preProcess(self, wordList):
        wordDict = collections.defaultdict(lambda: [])
        for word in wordList:
            for i in range(len(word)):
                wordDict[word[:i] + '_' + word[i + 1:]].append(word)
        return wordDict
