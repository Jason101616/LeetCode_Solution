# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

# For example:

# Given "aacecaaa", return "aaacecaaa".

# Given "abcd", return "dcbabcd".

# TLE
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        re_s = s[::-1]
        for i in range(len(s), 0, -1):
            if s[:i] == re_s[len(s) - i:]:
                return s[i:][::-1] + s
        return ''
