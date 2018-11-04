# Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
# If there isn't one, return 0 instead.

# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

# Example 1:
# Given nums = [1, -1, 5, -2, 3], k = 3,
# return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

# Example 2:
# Given nums = [-2, -1, 2, 1], k = 1,
# return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

# Follow Up:
# Can you do it in O(n) time?


# clarify: the subarray must be continious
# idea: use a hash table in which current sum is the key, current index is the value.
# If current sum minus k in the hash table, then we get one possible answer.
# Time:  O(n)
# Space: O(n)
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {}
        cur_sum, max_len = 0, 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum not in sums:
                sums[cur_sum] = i
            if cur_sum == k:
                max_len = i + 1
            elif (cur_sum - k) in sums:
                max_len = max(max_len, i - sums[cur_sum - k])

        return max_len
