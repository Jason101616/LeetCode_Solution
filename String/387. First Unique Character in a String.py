# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

# time: O(n)
# space: O(n)
# idea: traverse it one time and calculate the number
import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = collections.defaultdict(lambda: 0)
        for i in range(len(s)):
            counts[s[i]] += 1
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1
