# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5

# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0

# In this case, no transaction is done, i.e. max profit = 0.


class Solution(object):
    # 思路：
    # 用一个变量记录最小值，一个变量记录当前max profit
    # 然后遍历即可
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        smallest = float('inf')
        max_profit = 0
        for price in prices:
            if price < smallest:
                smallest = price
            elif price - smallest > max_profit:
                max_profit = price - smallest

        return max_profit
