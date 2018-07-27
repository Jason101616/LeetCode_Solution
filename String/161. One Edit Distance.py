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
        if len(s) < len(t): # make sure s is the longer string
            s, t = t, s

        for i in range(len(t)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    if i == len(t) - 1:
                        return True
                    else:
                        return s[i + 1:] == t[i + 1:]
                else:
                    return s[i + 1:] == t[i:]
        return len(s) - len(t) == 1
