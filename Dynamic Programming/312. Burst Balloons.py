# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect by bursting the balloons wisely.

# Note: 
# (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

# Example:

# Given [3, 1, 5, 8]

# Return 167

#     nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#    coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

# baseline1: Brute force. Burst the ballon in the nums one by one, then recurse. TLE.
# time: O(n!)
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        res = float('-inf')
        for i in range(len(nums)):
            if i == 0:
                tmp = nums[i] * nums[i + 1]
            elif i == len(nums) - 1:
                tmp = nums[i] * nums[i - 1]
            else:
                tmp = nums[i - 1] * nums[i] * nums[i + 1]
            res = max(res, tmp + self.maxCoins(nums[:i] + nums[i + 1:]))
        return res


# baseline2: Brute forece with memo. Still TLE.
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        return self.find_max_coins(nums, memo)

    def find_max_coins(self, nums, memo):
        if tuple(nums) in memo:
            return memo[tuple(nums)]
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        res = float('-inf')
        for i in range(len(nums)):
            if i == 0:
                tmp = nums[i] * nums[i + 1]
            elif i == len(nums) - 1:
                tmp = nums[i] * nums[i - 1]
            else:
                tmp = nums[i - 1] * nums[i] * nums[i + 1]
            res = max(res, tmp + self.maxCoins(nums[:i] + nums[i + 1:]))
        memo[tuple(nums)] = res
        return res


# thinking process: Regard balloon i as the last balloon of all to burst, the left and right section now has well defined boundary and do not affect each other.
# Solution 1: up-bottom dp with memo
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums[:] + [1]
        memo = [[None for _ in range(len(nums))] for __ in range(len(nums))]
        return self.find_max_coins(nums, memo, 0, len(nums) - 1)

    def find_max_coins(self, nums, memo, left, right):
        if left + 1 == right:
            return 0
        if memo[left][right] != None:
            return memo[left][right]
        res = 0
        for i in range(left + 1, right):
            res = max(res, nums[left] * nums[i] * nums[right] + self.find_max_coins(nums, memo, left,
                                                                                    i) + self.find_max_coins(nums, memo,
                                                                                                             i, right))
        memo[left][right] = res
        return res


# Solution 2: bottom-up dp
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums[:] + [1]
        dp = [[0 for _ in range(len(nums))] for __ in range(len(nums))]
        for k in range(2, len(nums)):  # interval length
            for left in range(len(nums) - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][len(nums) - 1]
