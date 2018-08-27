# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# idea: f[k, ii] represents the max profit up until prices[ii]
# (Note: NOT ending with prices[ii]) using at most k transactions.
# f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
#          = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
# f[0, ii] = 0; 0 times transaction makes 0 profit
# f[k, 0] = 0; if there is only one price data point you can't make any money no matter how many times you can trade
# time: O(kn), where k is the number of transactions

# intuitive solution (TLE):
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
            for j in range(1, len(prices)):
                tmp_max = float('-inf')
                for k in range(j):
                    tmp_max = max(dp[i - 1][k] - prices[k], tmp_max)
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmp_max)
        return dp[-1][-1]

# optimized solution:
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
            tmp_max = dp[i - 1][0] - prices[0]  # buy in price 0
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmp_max)
                tmp_max = max(tmp_max, dp[i - 1][j] - prices[j])    # previous tmp_max is known, thus saving some time
        return dp[-1][-1]
