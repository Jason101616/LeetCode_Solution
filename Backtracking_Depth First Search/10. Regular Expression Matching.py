# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

# Solution 1: Recursion
# idea: If a star is present in the pattern, it will be in the second position pattern[1]. Then, we may ignore this part of the pattern, or delete a matching character in the text. If we have a match on the remaining strings after any of these operations, then the initial inputs matched.
# a little tricky, see https://leetcode.com/problems/regular-expression-matching/solution/ for details
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        first_char_match = len(s) > 0 and (p[0] == s[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_char_match and self.isMatch(s[1:], p)
        else:
            return first_char_match and self.isMatch(s[1:], p[1:])


# Solution 2: DP
# idea: dp, top-down
# RecursionError: maximum recursion depth exceeded in comparison...
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        return self.match(s, 0, p, 0, memo)

    def match(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == len(p):
            ans = True if i == len(s) else False
        else:
            first_char_match = i < len(s) and p[j] == s[i] or p[j] == '.'
            if j + 1 < len(p) and p[j + 1] == '*':
                # pattern move 2 and string stay still or first_char_match and pattern stay still and string move 1
                ans = self.match(s, i, p, j + 2, memo) or first_char_match and self.match(s, i + 1, p, j, memo)
            else:
                ans = first_char_match and self.match(s, i + 1, p, j + 1, memo)
        memo[(i, j)] = ans
        return ans

# Solution 3: DP
# idea: dp, botton-up...
# see: https://discuss.leetcode.com/topic/6183/my-concise-recursive-and-dp-solutions-with-full-explanation-in-c
