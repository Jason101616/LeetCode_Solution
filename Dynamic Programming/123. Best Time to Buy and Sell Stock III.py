# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# idea: f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions. 
# f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
#          = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
# f[0, ii] = 0; 0 times transation makes 0 profit
# f[k, 0] = 0; if there is only one price data point you can't make any money no matter how many times you can trade
# time: O(kn), where k is the number of transactions
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        trans = 2
        dp = [[0 for _ in range(len(prices))] for __ in range(trans + 1)]
        for i in range(1, trans + 1):
            tmp_max = dp[i - 1][0] - prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmp_max)
                tmp_max = max(tmp_max, dp[i - 1][j] - prices[j])
        return dp[-1][-1]
