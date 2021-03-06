# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 

# idea: The essence of this problem is the conversion between 10 and 26 base.
from collections import deque


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = deque()
        while n:
            n -= 1
            tmp_char = chr(n % 26 + ord('a'))
            ret.appendleft(tmp_char.upper())
            n = n // 26

        return ''.join(ret)
