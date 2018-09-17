# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# Example 1:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.


# the same idea as 159 Longest Substring with At Most Two Distinct Characters
# idea: maintain a hashtable, with key is character, value is the number of time it appear in the substring
# also maintain a left pointer, if the number of element in the dictionary is larger than 2,
# the left pointer will be responsible for deleting some characters

from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        charCnt = defaultdict(lambda: 0)
        leftIdx, maxLen = 0, 0
        for idx, char in enumerate(s):
            charCnt[char] += 1
            while len(charCnt) > k:
                charCnt[s[leftIdx]] -= 1
                if charCnt[s[leftIdx]] == 0:
                    del charCnt[s[leftIdx]]
                leftIdx += 1
            maxLen = max(maxLen, idx - leftIdx + 1)
        return maxLen

