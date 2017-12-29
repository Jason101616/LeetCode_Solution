# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]

# You should return the indices: [0,9].
# (order does not matter).

# idea: maintain a dictionary and a sliding window
# refer to: http://www.cnblogs.com/grandyang/p/4521224.html
# there are wl(word len) times travel
# each time, n/wl words, mostly 2 times travel for each word
# one left side of the window, the other right side of the window
# so, time complexity O(wl * 2 * N/wl) = O(2N)
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # compute word occurences
        word_dict = collections.defaultdict(lambda: 0)
        for word in words:
            word_dict[word] += 1
        cnt = len(words)
        # traverse the s to find match
        word_len = len(words[0])
        res = []
        for i in range(word_len):
            left, count = i, 0
            cnt_dict = collections.defaultdict(lambda: 0)
            for j in range(i, len(s) - word_len + 1, word_len):
                sub_str = s[j: j + word_len]
                if sub_str in word_dict:
                    cnt_dict[sub_str] += 1
                    count += 1
                    # move the sliding window
                    while cnt_dict[sub_str] > word_dict[sub_str]:
                        new_sub_str = s[left: left + word_len]
                        cnt_dict[new_sub_str] -= 1
                        left += word_len
                        count -= 1
                    if count == cnt:
                        res.append(left)
                        cnt_dict[s[left: left + word_len]] -= 1
                        count -= 1
                        left += word_len
                else:
                    cnt_dict.clear()
                    left = j + word_len
                    count = 0
        return res