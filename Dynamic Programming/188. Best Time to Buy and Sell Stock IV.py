# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most k transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        if k > len(prices) // 2 + 1:
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

        dp = [[0 for _ in range(len(prices))] for __ in range(2)]
        for i in range(1, k + 1):
            tmp_max = dp[0][0] - prices[0]
            for j in range(1, len(prices)):
                dp[1][j] = max(dp[1][j - 1], prices[j] + tmp_max)
                tmp_max = max(tmp_max, dp[0][j] - prices[j])
            dp[0] = copy.deepcopy(dp[1])
        return dp[-1][-1]
