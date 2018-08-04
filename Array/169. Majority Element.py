# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.


# idea: we do not need to check the whole array to determine the answer.
# Although we are essentially removing this subarray from the original array, 
# the majority element will still be found in the rest of the array.

# time: O(n), space: O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for num in nums:
            if cnt == 0:
                res = num
            cnt += 1 if res == num else -1
        return res
