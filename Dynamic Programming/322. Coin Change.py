# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)

# Example 2:
# coins = [2], amount = 3
# return -1.

# Note:
# You may assume that you have an infinite number of each kind of coin.

# Approach 1: Top-bottom with memorization
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        memo = [[None for _ in range(amount + 1)] for __ in range(len(coins))]
        return self.find_change(coins, amount, 0, memo)

    def find_change(self, coins, amount, index, memo):
        if amount == 0:
            return 0
        if index >= len(coins):
            return -1
        if memo[index][amount] != None:
            return memo[index][amount]
        cur_coin = coins[index]
        max_coin_amount = amount // cur_coin
        res = float('inf')
        for i in range(max_coin_amount, -1, -1):
            cur_res = self.find_change(coins, amount - i * cur_coin, index + 1, memo)
            if cur_res != -1:
                res = min(res, cur_res + i)
        if res != float('inf'):
            memo[index][amount] = res
            return res
        memo[index][amount] = -1
        return -1


# Approach 2: bottom-up dp
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1