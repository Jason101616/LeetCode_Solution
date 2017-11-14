# Note: This is an extension of House Robber.

# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.


# idea: discuss two conditions, rob the first house or not
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev1 = prev2 = 0
        nums1 = nums[:-1]
        nums2 = nums[1:]
        for num in nums1:
            cur = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = cur
        ans0 = cur

        prev1 = prev2 = 0
        for num in nums2:
            cur = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = cur
        ans1 = cur
        return max(ans0, ans1)