# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# idea: f(k) = max(f(k – 2) + Ak, f(k – 1))
# Solution1: 
# time: O(n)
# space: O(n)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        len_num = len(nums)
        answer = [None] * len_num
        answer[0] = nums[0]
        answer[1] = max(nums[0], nums[1])
        for i in range(2, len_num):
            answer[i] = max(answer[i - 1], answer[i - 2] + nums[i])
        return answer[len_num - 1]

# time: O(n)
# space: O(1)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev2, prev1 = 0, 0
        for num in nums:
            cur = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = cur
        return cur
        