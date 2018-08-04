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

# Approach 1: BFS with storing the path. Space complexity is very high.
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
                            word_queue.append(
                                (word, cur_word[1] + [word]))  # use a very high space complexity to store the path
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


# Approach 2: Bi-directional BFS
# bi-directional BFS
# basic idea:
# 1. maintain seperates queue, visited hash set for each direction
# 2. for each string(node), create a PathNode class to store its previous node
# 3. To find all the path during BFS, we should not stop searching when we find one answer in the current layer.
# 4. When there is at least one intersection in the two BFS queue, we find the answer.
class PathNode:
    def __init__(self, string, previous):
        self.string = string
        self.previous = [previous]


class BFSQueue:
    def __init__(self, init_words):
        self.queue = collections.deque()
        self.visited = {}
        for PathNode in init_words:
            self.queue.append(PathNode)
            self.visited[PathNode.string] = PathNode

    def size(self):
        return len(self.queue)


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        neighbors = self.preprocess(wordList)
        forward_queue = BFSQueue([PathNode(beginWord, None)])
        backward_queue = BFSQueue([PathNode(endWord, None)])
        while not self.is_intersect(forward_queue, backward_queue) and (
                forward_queue.size() > 0 or backward_queue.size() > 0):
            if 0 < forward_queue.size() <= backward_queue.size():
                self.search(forward_queue, neighbors)
            else:
                self.search(backward_queue, neighbors)
        return self.merge_queue(forward_queue, backward_queue)

    def merge_queue(self, forward_queue, backward_queue):
        def find_path(string, BFS_Q):
            def helper(path_node):
                if not path_node:
                    return []
                helper_res = []
                for node in path_node.previous:
                    helper_res.extend(helper(node))
                if not helper_res:
                    helper_res.append([path_node.string])
                else:
                    for i in range(len(helper_res)):
                        helper_res[i].append(path_node.string)
                return helper_res

            return helper(BFS_Q.visited[string])

        def merge_path(forward, backward):
            merge_res = []
            for path0 in forward:
                for path1 in backward:
                    merge_res.append(path0[:-1] + path1[::-1])
            return merge_res

        intersect = set(forward_queue.visited.keys()) & set(backward_queue.visited.keys())
        ret = []
        for string in intersect:
            path_forward = find_path(string, forward_queue)
            path_backward = find_path(string, backward_queue)
            ret.extend(merge_path(path_forward, path_backward))
        return ret

    def search(self, bfs_q, neighbors):
        length = bfs_q.size()
        tmp_visited = {}  # in order to get all the paths, we should update visited at the end
        for i in range(length):
            cur_word = bfs_q.queue.popleft()
            for i in range(len(cur_word.string)):
                next_words = neighbors[cur_word.string[:i] + '_' + cur_word.string[i + 1:]]
                for word in next_words:
                    if word not in bfs_q.visited:
                        if word not in tmp_visited:
                            tmp_visited[word] = PathNode(word, cur_word)
                        else:
                            tmp_visited[word].previous.append(cur_word)
        for word in tmp_visited:
            bfs_q.queue.append(tmp_visited[word])
        bfs_q.visited.update(tmp_visited)

    def preprocess(self, wordList):
        word_dict = collections.defaultdict(lambda: [])
        for word in wordList:
            for i in range(len(word)):
                tmp = word[:i] + '_' + word[i + 1:]
                word_dict[tmp].append(word)
        return word_dict

    def is_intersect(self, BFSQueue1, BFSQueue2):
        return set(BFSQueue1.visited.keys()) & set(BFSQueue2.visited.keys())
