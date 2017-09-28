# Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
# Note: Length of the array will not exceed 10,000.

# Idea: Use a pointer to traverse the list.
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return 1
        
        index = 1
        LCI = 1
        cur_len = 1
        while index < length:
            if nums[index] > nums[index - 1]:
                cur_len += 1
            else:
                if cur_len > LCI:
                    LCI = cur_len
                cur_len = 1
            index += 1
        if cur_len > LCI:
            LCI = cur_len
        return LCI
            