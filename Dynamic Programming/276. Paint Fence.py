# idea: simple iteration
class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # cur same = prev diff
        # cur diff = pref diff * (k-1) + prev_same * (k-1)
        if n == 0:
            return 0
        elif n == 1:
            return k
        cur_same = k
        cur_diff = k * (k - 1)
        for i in range(2, n):
            prev_same, prev_diff = cur_same, cur_diff
            cur_same = prev_diff
            cur_diff = (k - 1) * (prev_diff + prev_same)
        return cur_same + cur_diff
