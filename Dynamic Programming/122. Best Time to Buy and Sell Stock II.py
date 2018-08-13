# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


# Solution 1: Simple One Pass
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


# Solution 2: Peak Valley Approach
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        len_prices = len(prices)
        ans = 0
        valley = 0
        peak = self.find_peak(0, prices)
        while peak != -1 and valley != -1:
            ans += prices[peak] - prices[valley]
            valley = self.find_valley(peak + 1, prices)
            if valley != -1:
                peak = self.find_peak(valley + 1, prices)
        return ans

    def find_valley(self, index, prices):
        if index >= len(prices):
            return -1
        while index + 1 < len(prices) and prices[index + 1] <= prices[index]:
            index += 1
        return index

    def find_peak(self, index, prices):
        if index >= len(prices):
            return -1
        while index + 1 < len(prices) and prices[index + 1] >= prices[index]:
            index += 1
        return index
