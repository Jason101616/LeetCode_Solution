# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output:  321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

import math


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_val = -math.pow(2, 31)
        max_val = math.pow(2, 31) - 1
        is_negative = False
        if x < 0:
            is_negative = True
        x = abs(x)
        x = int(str(x)[::-1])
        if is_negative:
            x = -x
        return 0 if x < min_val or x > max_val else x

# C++
class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x != 0) {
            if (abs(res) > INT_MAX / 10) return 0;
            res = res * 10 + x % 10;
            x /= 10;
        }
        return res;
    }
};