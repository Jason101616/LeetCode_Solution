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

from collections import defaultdict
class Solution:
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    def findLadders(self, start, end, words_list):
        wordLen = len(start)
        front, back = defaultdict(list), defaultdict(list)
        front[start].append([start])
        back[end].append([end])
        # remove start from dict, add end to dict if it is not there
        dict = set(words_list)
        dict.discard(start)
        if end not in dict:
            dict.add(end)
        forward, result = True, []
        while front:
            # get all valid transformations
            nextSet = defaultdict(list)
            for word, paths in front.items():
                for index in range(wordLen):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = word[:index] + ch + word[index+1:]
                        if nextWord in dict:
                            # update paths
                            if forward:
                                # append next word to path
                                tmp = [path + [nextWord] for path in paths]
                                nextSet[nextWord].extend(tmp)
                            else:
                                # add next word in front of path
                                nextSet[nextWord].extend([[nextWord] + path for path in paths])
            front = nextSet
            common = set(front) & set(back)
            if common:
                # path is through
                if not forward:
                    # switch front and back if we were searching backward
                    front, back = back, front
                result.extend([head + tail[1:] for word in common for head in front[word] for tail in back[word]])
                return result

            if len(front) > len(back):
                # swap front and back for better performance (smaller nextSet)
                front, back, forward = back, front, not forward

            # remove transformations from wordDict to avoid cycles
            dict -= set(front)

        return []
