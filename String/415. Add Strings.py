# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        num1, num2 = num1[::-1], num2[::-1]
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num2 += "0" * (len(num1) - len(num2))
        add = 0
        for i in range(len(num2)):
            curNum = int(num1[i]) + int(num2[i]) + add
            add = 0
            if curNum > 9:
                curNum -= 10
                add = 1
            res.append(str(curNum))
        if add > 0:
            res.append("1")
        return ''.join(res)[::-1]
