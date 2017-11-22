# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

# Note that 1 is typically treated as an ugly number, and n does not exceed 1690.


# An ugly number is generated from the previous ugly number times by 2, 3 or 5. Every time choose the minimum value from the three lists
# (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
# (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
# (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        ans = [1]
        i2 = i3 = i5 = 0
        while len(ans) < n:
            tmp2, tmp3, tmp5 = ans[i2] * 2, ans[i3] * 3, ans[i5] * 5
            min_tmp = min(tmp2, tmp3, tmp5)
            if min_tmp == tmp2:
                i2 += 1
            if min_tmp == tmp3:
                i3 += 1
            if min_tmp == tmp5:
                i5 += 1
            ans.append(min_tmp)
        return ans[n - 1]