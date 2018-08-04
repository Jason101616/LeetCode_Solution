# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

# Solution: simple recursion
# time: O(2^len(nums))
# result: TLE
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.num = 0
        self.findTarget(nums, S, 0, 0)
        return self.num

    def findTarget(self, nums, S, index, prev_ans):
        if index == len(nums):
            if prev_ans == S:
                self.num += 1
            return
        self.findTarget(nums, S, index + 1, prev_ans + nums[index])
        self.findTarget(nums, S, index + 1, prev_ans - nums[index])


# Solution: top-down with memory
# time: O(2001 * len(nums))
# result: Accepted
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.memo = [[None for _ in range(2001)] for __ in range(len(nums))]
        return self.findTarget(nums, S, 0, 0)

    def findTarget(self, nums, S, index, prev_ans):
        if index == len(nums):
            if prev_ans == S:
                return 1
            else:
                return 0
        if self.memo[index][prev_ans + 1000] != None:
            return self.memo[index][prev_ans + 1000]
        plus_ans = self.findTarget(nums, S, index + 1, prev_ans + nums[index])
        minus_ans = self.findTarget(nums, S, index + 1, prev_ans - nums[index])
        self.memo[index][prev_ans + 1000] = plus_ans + minus_ans
        return self.memo[index][prev_ans + 1000]

    # Solution: 2D Dynamic Programming


# time: O(2001 * len(nums))
# result: TLE
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        len_sum = len(nums)
        dp = [[0 for _ in range(2001)] for __ in range(len_sum)]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, len_sum):
            for j in range(-1000, 1001):
                if dp[i - 1][j + 1000] > 0:
                    dp[i][j + 1000 + nums[i]] += dp[i - 1][j + 1000]
                    dp[i][j + 1000 - nums[i]] += dp[i - 1][j + 1000]
        return dp[len_sum - 1][S + 1000] if S <= 1000 else 0


# Solution: 1D Dynamic Programming
# time: O(2001 * len(nums))
# result: TLE
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        len_sum = len(nums)
        dp = [0 for _ in range(2001)]
        dp_next = [0 for _ in range(2001)]
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        for i in range(1, len_sum):
            for j in range(-1000, 1001):
                if dp[j + 1000] > 0:
                    dp_next[j + 1000 + nums[i]] += dp[j + 1000]
                    dp_next[j + 1000 - nums[i]] += dp[j + 1000]
            dp = dp_next
            dp_next = [0 for _ in
                       range(2001)]  # this line is important, otherwise dp and dp_next point to the same memory
        return dp[S + 1000] if S <= 1000 else 0
