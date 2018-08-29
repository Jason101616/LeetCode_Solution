# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

# Time:  O(n^2)
# Space: O(n^2)
# idea: dynamic programming
# dp[i, j] = 1                                   if i == j
#          = s[i] == s[j]                        if j = i + 1
#          = s[i] == s[j] && dp[i + 1][j - 1]    if j > i + 1      


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        dp = [[False for _ in range(len(s))] for __ in range(len(s))]
        left, right, maxLen = 0, 1, 1
        for i in range(len(s)):
            for j in range(i):
                if i - j <= 2:
                    dp[j][i] = (s[i] == s[j])
                else:
                    dp[j][i] = (s[i] == s[j] and dp[j + 1][i - 1])
                if dp[j][i] and i - j + 1 > maxLen:
                    maxLen, left, right = i - j + 1, j, i + 1
            dp[i][i] = True

        return s[left:right]
