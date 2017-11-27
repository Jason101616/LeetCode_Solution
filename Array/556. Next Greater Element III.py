# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

# Example 1:
# Input: 12
# Output: 21
# Example 2:
# Input: 21
# Output: -1


# idea: very similar to next permutation, be careful about the 32-bit limitation
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        while n > 0:
            nums.append(n % 10)
            n = n // 10
        nums = nums[::-1]

        if len(nums) < 2:
            return -1
        # find from right, the first element smaller than its right element. mark the pos
        # if pos < 0, rearrange it as the lowest possible order
        pos = len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pos = i
                break
        if pos == len(nums):
            return -1
        else:
            # start from pos to right, find the pos2, which satisfy nums[pos2] > nums[pos] >= nums[pos2+1]
            pos2 = len(nums) - 1
            for i in range(pos + 1, len(nums) - 1):
                if nums[i] > nums[pos] and nums[pos] >= nums[i + 1]:
                    pos2 = i
                    break
            # swap element in pos and pos2
            nums[pos], nums[pos2] = nums[pos2], nums[pos]
            # reverse the number start from pos+1
            nums[pos + 1:] = sorted(nums[pos + 1:])
        ret = 0
        for i in range(len(nums) - 1, -1, -1):
            ret += nums[i] * pow(10, len(nums) - 1 - i)
        return ret if ret < pow(2, 31) else -1