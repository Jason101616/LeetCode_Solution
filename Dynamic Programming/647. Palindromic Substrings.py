# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.


# Time:  O(n^2)
# Space: O(n^2)
# idea: dynamic programming, nearly the same solution as Longest Palindromic Substring
# dp[i, j] = 1                                   if i == j
#          = s[i] == s[j]                        if j = i + 1
#          = s[i] == s[j] && dp[i + 1][j - 1]    if j > i + 1     
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        memo = [[False for _ in range(len(s))] for __ in range(len(s))]
        for i in range(len(s)):
            for j in range(i):
                if i - j <= 2:
                    memo[j][i] = (s[j] == s[i])
                else:
                    memo[j][i] = (s[j] == s[i] and memo[j + 1][i - 1])
                if memo[j][i]:
                    cnt += 1
            memo[i][i] = True
            cnt += 1
            
        return cnt
        