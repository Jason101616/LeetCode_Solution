# Implement int sqrt(int x).

# Compute and return the square root of x.

# Time:  O(logn)
# Space: O(1)
# 思路：确定左右范围，暴力二分查找。

import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        left = 1
        right = x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1
