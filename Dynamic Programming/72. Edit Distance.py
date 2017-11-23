# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:

# a) Insert a character
# b) Delete a character
# c) Replace a character


# idea: dp
# let dp[i][j] denote edit distance between word1[0, i - 1] and word2[0, j - 1]
# if word1[i - 1] == word2[j - 1], then p[i][j] = p[i - 1][j - 1]
# else p[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
# where dp[i - 1][j - 1] can be seen as replacement,
# dp[i - 1][j] can be seen as delete one char of word1 or insert one char in word2
# dp[i][j - 1] can be seen as delete one char of word2 or insert one char in word1
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if not word1:
            return n
        if not word2:
            return m
        dp = [[None for _ in range(n + 1)] for __ in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j],
                                   dp[i][j - 1]) + 1
        return dp[m][n]