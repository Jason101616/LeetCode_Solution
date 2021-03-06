# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

# Note: You can assume that

# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
 

# Example 1:

# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
 

# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
 

# Example 3:

# Input: amount = 10, coins = [10] 
# Output: 1

# top down dp with memorization
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if not coins:
            if amount == 0:
                return 1
            else:
                return 0
        coins.sort(reverse=True)
        return self.dfs(amount, 0, 0, coins, {})

    def dfs(self, amount, curAmount, idx, coins, memo):
        if curAmount == amount:
            return 1
        if amount - curAmount < coins[-1]:
            return 0
        if (amount - curAmount, idx) in memo:
            return memo[(amount - curAmount, idx)]
        res = 0
        for i in range(idx, len(coins)):
            res += self.dfs(amount, curAmount + coins[i], i, coins, memo)
        memo[(amount - curAmount, idx)] = res
        return res

# Knapsack problem
# https://leetcode.com/problems/coin-change-2/discuss/99212/Knapsack-problem-Java-solution-with-thinking-process-O(nm)-Time-and-O(m)-Space
# This is a classic knapsack problem. Honestly, I'm not good at knapsack problem, it's really tough for me.

# dp[i][j] : the number of combinations to make up amount j by using the first i types of coins
# State transition:

# not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
# using the ith coin, since we can use unlimited same coin, we need to know how many way to make up amount j - coins[i] by using first i coins(including ith), which is dp[i][j-coins[i]]
# Initialization: dp[i][0] = 1

# Once you figure out all these, it's easy to write out the code:

#     public int change(int amount, int[] coins) {
#         int[][] dp = new int[coins.length+1][amount+1];
#         dp[0][0] = 1;
        
#         for (int i = 1; i <= coins.length; i++) {
#             dp[i][0] = 1;
#             for (int j = 1; j <= amount; j++) {
#                 dp[i][j] = dp[i-1][j] + (j >= coins[i-1] ? dp[i][j-coins[i-1]] : 0);
#             }
#         }
#         return dp[coins.length][amount];
#     }
# Now we can see that dp[i][j] only rely on dp[i-1][j] and dp[i][j-coins[i]], then we can optimize the space by only using one-dimension array.

#     public int change(int amount, int[] coins) {
#         int[] dp = new int[amount + 1];
#         dp[0] = 1;
#         for (int coin : coins) {
#             for (int i = coin; i <= amount; i++) {
#                 dp[i] += dp[i-coin];
#             }
#         }
#         return dp[amount];
#     }
