# Given an unsorted array of integers, find the number of longest increasing subsequence.

# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
# Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

# idea: dp, 用length[i]表示以nums[i]为结尾的递推序列的长度，用count[i]表示以nums[i]为结尾的递推序列的个数，初始化都赋值为1，只要有数字，那么至少都是1。
# time: O(n^2)
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = [1 for _ in range(len(nums))]
        count = list(length)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] >= length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]
        max_len = max(length)
        index_max_len = [i for i in range(len(length)) if length[i] == max_len]
        res = 0
        for index in index_max_len:
            res += count[index]
        return res
