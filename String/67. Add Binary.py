# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 思路：
        # invoke python builtin API. The power of Python.
        return bin(int(a, 2) + int(b, 2))[2:]