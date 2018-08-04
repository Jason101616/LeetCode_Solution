# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        res = float('inf')
        sum_cur = 0
        while r <= len(nums):
            if sum_cur < s:
                if r >= len(nums):
                    break
                sum_cur += nums[r]
                r += 1
                continue
            res = min(res, r - l)
            sum_cur -= nums[l]
            l += 1
        return res if res != float('inf') else 0
