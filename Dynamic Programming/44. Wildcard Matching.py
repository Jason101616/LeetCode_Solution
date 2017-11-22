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


# Solution 1: DFS
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
            return self.is_all(p)
        if len(s) > 0 and p[0] == s[0] or p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        elif p[0] == '*':
            return self.isMatch(s, p[1:]) or self.isMatch(
                s[1:], p[1:]) or self.isMatch(s[1:], p)
        else:
            return False

    def is_all(self, string):
        for char in string:
            if char != '*':
                return False
        return True