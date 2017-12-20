# Given two strings S and T, determine if they are both one edit distance apart.

# discuss this problem by the length of the two words
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) < len(t):
            s, t = t, s
        for i in range(len(t)):
            if s[i] != t[i]: 
                if len(s) != len(t):
                    return s[i + 1:] == t[i:]
                elif i + 1 <= len(t) - 1:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return True
        return len(s) - len(t) == 1