# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

# idea: BFS with marking the path
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordDict = self.pre_process(wordList)
        word_set = set(wordList)
        word_queue = collections.deque()
        word_queue.append((beginWord, [beginWord]))
        find_ans = False
        res = []
        while word_queue:
            if find_ans:
                break
            size = len(word_queue)
            remove_set = set()
            for i in range(size):
                cur_word = word_queue.popleft()
                if cur_word[0] == endWord:
                    find_ans = True
                    res.append(cur_word[1])
                for j in range(len(cur_word[0])):
                    part_word = cur_word[0][:j] + '_' + cur_word[0][j + 1:]
                    neighword_words = wordDict[part_word]
                    for word in neighword_words:
                        if word in word_set:
                            word_queue.append((word, cur_word[1] + [word]))
                            remove_set.add(word)
            word_set -= remove_set
        return res

    def pre_process(self, word_list):
        word_dict = collections.defaultdict(lambda: [])
        for word in word_list:
            for i in range(len(word)):
                s = word[:i] + '_' + word[i + 1:]
                word_dict[s].append(word)
        return word_dict

