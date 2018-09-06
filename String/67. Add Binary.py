# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

# This implementation support any number of binary number
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        binaryNum = [a, b]
        maxIdx = 0
        for binary in binaryNum:
            if len(binary) - 1 > maxIdx:
                maxIdx = len(binary) - 1

        idx, carry = 0, 0
        res = deque()
        while True:
            if idx > maxIdx and carry == 0:
                break
            curRes = carry
            for binary in binaryNum:
                if idx < len(binary):
                    curRes += int(binary[len(binary) - 1 - idx])
            res.appendleft(curRes % 2)
            carry = curRes // 2
            idx += 1
        res = [str(num) for num in res]
        return ''.join(res)
