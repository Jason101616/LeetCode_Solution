# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        res = 0
        i = 0
        while s:
            char = s.pop()
            res += (ord(char) - ord('A') + 1) * pow(26, i)
            i += 1
        return res
