# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output:  2
# Explanation:  There are two ways to climb to the top.

# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output:  3
# Explanation:  There are three ways to climb to the top.

# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# Solution 1: Recursion with memorization
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = [0] * n
        return self.find_ans(0, n)

    def find_ans(self, cur_step, target_step):
        if cur_step > target_step:
            return 0
        if cur_step == target_step:
            return 1
        if self.memo[cur_step] > 0:
            return self.memo[cur_step]
        ans = self.find_ans(cur_step + 1, target_step) + self.find_ans(
            cur_step + 2, target_step)
        self.memo[cur_step] = ans
        return ans


# Solution 2: Dynamic programmming
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
