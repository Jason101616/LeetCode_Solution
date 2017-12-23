# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

# idea: use a hash map to jot down the number of 1 and 0 enountered till now. key is the sum, value is the index.
# when encounter a 1, plus 1, when encounter 0, minus 1. 
# Thus, if the sum was in the hash map before, index - previous index can be a candidate answer.
# The minimum candidate answer is the answer.
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_dict = {}
        cur_sum = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur_sum -= 1
            else:
                cur_sum += 1
            if cur_sum == 0:
                res = max(res, i + 1)
            if cur_sum not in cnt_dict:
                cnt_dict[cur_sum] = i
            else:
                res = max(res, i - cnt_dict[cur_sum])
        return res
            