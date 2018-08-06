# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor or (dividend == (-1) * (1 << 31) and divisor == -1):
            return (1 << 31) - 1
        sign = (dividend < 0) ^ (divisor < 0)  # 1 is negative, 0 is positive
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmpRes, tmpDivisor = 1, divisor
            while dividend >= (tmpDivisor << 1):
                tmpDivisor <<= 1
                tmpRes <<= 1
            res += tmpRes
            dividend -= tmpDivisor
        return res if not sign else -res
