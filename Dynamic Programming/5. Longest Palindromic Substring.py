# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.
# Example:

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
        memo = [[False for _ in range(len(s))] for __ in range(len(s))]
        left, right, max = 0, 1, 1
        for i in range(len(s)):
            for j in range(i):
                if i - j <= 2:
                    memo[j][i] = (s[i] == s[j])
                else:
                    memo[j][i] = (s[i] == s[j] and memo[j + 1][i - 1])
                if memo[j][i] and i - j + 1 > max:
                    max, left, right = i - j + 1, j, i + 1
            memo[i][i] = True

        return s[left:right]
