# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:

# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]


# dp, maintain three transition function.
# one is sell[i], which means what we can earn most if before(include) the i th day the last operation is selling the product
# another is buy[i], which means what we can earn most if before(include) the i th day the last operation is buying the product
# third is cooldown[i], which means what we can earn most if before(include) the i th day the last operation is cooling down
# sell[i] = max(buy[i - 1] + price[i], sell[i - 1]), where sell[i - 1] means we do nothing in the i th day, buy[i - 1] means we buy a product in i - 1 th day and sell the product in the i th day.
# buy[i] = max(cooldown[i - 1] - price[i], buy[i - 1])
# cooldown[i] = sell[i - 1]
# from previous three equations, we come up with the following two equations:
# sell[i] = max(buy[i - 1] + price[i], sell[i - 1])
# buy[i] = max(sell[i - 2] - price[i], buy[i - 1])
# answer is sell[len(prices) - 1], now we can write the code
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_prices = len(prices)
        if len_prices <= 1:
            return 0
        sell = [None for _ in range(len_prices)]
        buy = [None for _ in range(len_prices)]
        sell[0] = 0
        buy[0] = -prices[0]
        sell[1] = max(buy[0] + prices[1], sell[0])
        buy[1] = max(-prices[1], buy[0])
        for i in range(2, len_prices):
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
            buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
        return sell[len_prices - 1]


# optimization, use O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_prices = len(prices)
        if len_prices <= 1:
            return 0
        sell0 = 0
        buy0 = -prices[0]
        sell1 = max(buy0 + prices[1], sell0)
        buy1 = max(-prices[1], buy0)
        for i in range(2, len_prices):
            sell2 = max(buy1 + prices[i], sell1)
            buy2 = max(sell0 - prices[i], buy1)
            sell0, buy0 = sell1, buy1
            sell1, buy1 = sell2, buy2
        return sell1
