# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

# Examples:
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
# Notes:
# You may assume both pattern and str contains only lowercase letters.

# time: O(m * (n-1)Cm), where n is the length of pattern, m is the length of str
# C means combination, (n-1)Cm = C(n-1)m
# idea: see https://discuss.leetcode.com/topic/26750/share-my-java-backtracking-solution?page=1
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        char_string_dict = {}
        string_set = set()
        return self.isMatch(str, 0, pattern, 0, char_string_dict, string_set)

    def isMatch(self, string, i, pattern, j, char_string_dict, string_set):
        if i == len(string) and j == len(pattern):
            return True
        if i == len(string) or j == len(pattern):
            return False

        if pattern[j] in char_string_dict:
            map_s = char_string_dict[pattern[j]]
            if string[i: i + len(map_s)] != map_s:
                return False
            else:
                return self.isMatch(string, i + len(map_s), pattern, j + 1, char_string_dict, string_set)

        for k in range(i, len(string)):
            sub_str = string[i: k + 1]
            if sub_str in string_set:
                continue
            char_string_dict[pattern[j]] = sub_str
            string_set.add(sub_str)
            if self.isMatch(string, k + 1, pattern, j + 1, char_string_dict, string_set):
                return True
            del char_string_dict[pattern[j]]
            string_set.remove(sub_str)

        return False

    你写java就行