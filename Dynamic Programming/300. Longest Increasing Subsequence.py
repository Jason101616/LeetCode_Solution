# Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

# Your algorithm should run in O(n2) complexity.

# Follow up: Could you improve it to O(n log n) time complexity?

# Solution 1: DP
# idea: for each num in nums, record the number of num smaller than it. Finally, pick the largest one in this dp list.
# time complexity: O(n^2)
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        len_nums = len(nums)
        dp = [1 for _ in range(len_nums)]
        for i in range(1, len_nums):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

# Solution 2: Binary Search + maintain a tail list
see https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation