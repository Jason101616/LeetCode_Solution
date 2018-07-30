# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false


# Solution 1: DFS(TLE)
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return s == ''
        if not s:
            return self.isAllAsterisk(p)
        if p[0] == s[0] or p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        elif p[0] == '*':
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p[1:]) or self.isMatch(s[1:], p)
        else:
            return False

    def isAllAsterisk(self, string):
        for char in string:
            if char != '*':
                return False
        return True

# Solution 2: Top-bottom DP
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = [[None for _ in range(len(p))] for __ in range(len(s))]
        return self.helper(s, 0, p, 0, memo)
    
    def helper(self, s, i, p, j, memo):
        if j == len(p):
            return i == len(s)
        if i == len(s):
            return self.isAllAsterisk(p, j)
        if memo[i][j] != None:
            return memo[i][j]
        if s[i] == p[j] or p[j] == '?':
            memo[i][j] = self.helper(s, i + 1, p, j + 1, memo)
            return memo[i][j]
        elif p[j] == '*':
            memo[i][j] = self.helper(s, i + 1, p, j, memo) or self.helper(s, i + 1, p, j + 1, memo) or self.helper(s, i, p, j + 1, memo)
            return memo[i][j]
        else:
            memo[i][j] = False
            return False
        
    def isAllAsterisk(self, p, j):
        for i in range(j, len(p)):
            if p[i] != '*':
                return False
        return True
        