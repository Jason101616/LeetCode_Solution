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
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        sum_dict = collections.defaultdict(lambda: 0)
        total_sum = 0
        for num in nums:
            total_sum += num
            if total_sum == k:
                res += 1
            res += sum_dict[total_sum - k]
            sum_dict[total_sum] += 1
        return res