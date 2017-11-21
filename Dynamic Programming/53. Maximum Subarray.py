# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


# idea: use dp. the recursive formula is dp[i] = max(dp[i - 1] + nums[i], nums[i])
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        len_nums = len(nums)
        dp = [0 for _ in range(len_nums)]
        dp[0] = nums[0]
        max_ans = dp[0]
        for i in range(1, len_nums):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            if dp[i] > max_ans:
                max_ans = dp[i]
        return max_ans