# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# Example 1:
# Given the following words in dictionary,

# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".

# Example 2:
# Given the following words in dictionary,

# [
#   "z",
#   "x"
# ]
# The correct order is: "zx".

# Example 3:
# Given the following words in dictionary,

# [
#   "z",
#   "x",
#   "z"
# ]
# The order is invalid, so return "".

# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# # idea: the essence of this problem is topological sort. if the topological sort exist, then answer exist.
# Firstly, we need to find the all the valid pairs to calculate the in-degree of each character.
# Secondly, push the character which has zero in-degree into a queue, also put these character into the answer
# delete those zero-in-degree character from the queue. in the meantime, update the in-degree of each character. Then push those character into the queue.
# finally, compare the length of the answer with the length of all the characters. If they are the same, return the answer, else return ''
# time: O(V+E) + O(n*k), where n is the length of the words, k is the longest length of a word, V is the number of vertices, E is the number of edge in the graph
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res = ''
        # put all the pairs into the set
        pair_set = set()
        for i in range(len(words) - 1):
            min_len = min(len(words[i]), len(words[i + 1]))
            cannot_compare = False
            for j in range(min_len):
                if words[i][j] != words[i + 1][j]:
                    pair_set.add((words[i][j], words[i + 1][j]))
                    break
                if j == min_len - 1:
                    cannot_compare = True
            if cannot_compare and len(words[i]) > min_len:
                return ''

        # put all the character into the char_dict, value is the in-degree
        char_dict = collections.defaultdict(lambda: 0)
        for word in words:
            for char in word:
                char_dict[char] = 0
        # calculate the in-degree of all the character
        for pair in pair_set:
            char_dict[pair[1]] += 1
        # maintain a queue
        queue = collections.deque()
        for char in char_dict.keys():
            if char_dict[char] == 0:
                queue.append(char)
                res += char
        # use topological sort to calculate the order
        while queue:
            cur_char = queue.popleft()
            for pair in pair_set.copy():
                if pair[0] == cur_char:
                    char_dict[pair[1]] -= 1
                    if char_dict[pair[1]] == 0:
                        pair_set.remove(pair)
                        res += pair[1]
                        queue.append(pair[1])

        return res if len(res) == len(char_dict) else ''