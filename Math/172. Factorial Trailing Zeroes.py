# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        i = 5
        while True:
            if n / 5 < 1:
                break
            res += (n // 5)
            n //= 5
            i *= 5
        return res