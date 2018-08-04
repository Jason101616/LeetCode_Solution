# Given a string s and a string t, check if s is subsequence of t.

# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# s = "abc", t = "ahbgdc"

# Return true.

# Example 2:
# s = "axc", t = "ahbgdc"

# Return false.

# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

# idea: use a dictionary to record the index of each character, and compare them one by one
from collections import defaultdict


class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.get_char_dict(t)
        min_index = -1
        for char in s:
            if char not in self.char_dict:
                return False
            index_in_list = self.insert_index(self.char_dict[char], min_index)
            if index_in_list == len(self.char_dict[char]):
                return False
            min_index = self.char_dict[char][index_in_list]
        return True

    def get_char_dict(self, t):
        self.char_dict = defaultdict(lambda: [])
        for index, char in enumerate(t):
            self.char_dict[char].append(index)

    def insert_index(self, index_list, min_index):
        for i, index in enumerate(index_list):
            if index > min_index:
                return i
        return len(index_list)
