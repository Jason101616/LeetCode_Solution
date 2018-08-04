# Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

# Note:
# If n is the length of array, assume the following constraints are satisfied:

# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# Examples:

# Input:
# nums = [7,2,5,10,8]
# m = 2

# Output:
# 18

# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

# Solution 1: dp
# idea: dp. dp[i][j] denote the largest sum of nums[0...i - 1] among j subarrays
# dp[i][j] = for all valid k {min[max(dp[k][j - 1], nums[k + 1] + ... + nums[i])]}
# one observation is that, nums[:i] can be divided into [1, i] parts
# time: O(n^2 * m)
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # sub_sum is the sum of the number in nums from 1 to i, inclusive
        sub_sum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(sub_sum)):
            sub_sum[i] = sub_sum[i - 1] + nums[i - 1]
        dp = [[float('inf') for _ in range(m + 1)] for __ in range(len(nums) + 1)]
        dp[0][0] = 0
        for i in range(1, len(nums) + 1):
            for j in range(1, min(i + 1, m + 1)):  # at most divided into i parts
                for k in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub_sum[i] - sub_sum[k]))
        return dp[-1][-1]

    # solution 2: binary search + Greedy. don't know how to write.
# see the answer
