# Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

# Your algorithm should run in O(n^2) complexity.

# Follow up: Could you improve it to O(n*logn) time complexity?


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
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


# Solution 2:
# idea: 先建立一个空的dp数组，然后开始遍历原数组，对于每一个遍历到的数字，我们用二分查找法在dp数组找第一个不小于它的数字，
# 如果这个数字不存在，那么直接在dp数组后面加上遍历到的数字，如果存在，则将这个数字更新为当前遍历到的数字，最后返回dp数字的长度即可，
# 注意的是，dp数组的值可能不是一个真实的LIS。
# time complexity: O(n*log(n))
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                l, r = 0, len(dp) - 1
                while l < r:
                    mid = l + (r - l) // 2
                    if dp[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid
                dp[l] = nums[i]
        return len(dp)
