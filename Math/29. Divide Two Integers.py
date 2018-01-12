# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor or (dividend == (-1) * (1 << 31) and divisor == -1):
            return (1 << 31) - 1
        sign = (dividend < 0) ^ (divisor < 0)   # 1 is negative, 0 is positive
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp_res, tmp_divisor = 1, divisor
            while dividend >= (tmp_divisor << 1):
                tmp_divisor <<= 1
                tmp_res <<= 1
            res += tmp_res
            dividend -= tmp_divisor
        return res if not sign else -res
        