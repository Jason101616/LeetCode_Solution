# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

# idea: traverse once, use a hashmap to store the current sum.
# when encounter a new number, check whether current sum - k is in the hashmap
# if in the hashmap, res + 1
from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumCnt = defaultdict(lambda: 0)
        curSum = res = 0
        for num in nums:
            curSum += num
            if curSum == k:
                res += 1
            res += sumCnt[curSum - k]
            sumCnt[curSum] += 1
        return res
