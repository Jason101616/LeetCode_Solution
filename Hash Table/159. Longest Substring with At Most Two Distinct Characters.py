# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
#
# Example 1:
#
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:
#
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.


# idea: hashtable + two pointers

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        charCnt = collections.defaultdict(lambda: 0)
        left = 0
        maxLen = 0
        for i in range(len(s)):
            charCnt[s[i]] += 1
            while len(charCnt) > 2:
                charCnt[s[left]] -= 1
                if charCnt[s[left]] == 0:
                    del charCnt[s[left]]
                left += 1
            maxLen = max(maxLen, i - left + 1)
        return maxLen
