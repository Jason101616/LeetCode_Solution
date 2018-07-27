# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Solve it without division and in O(n).

# For example, given [1,2,3,4], return [24,12,8,6].

# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

# curAns = prevAns / cur * prevNum
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in range(len(nums))]
        prevNum = nums[0]
        res[0] = self.calProduct(nums[1:])
        for i in range(1, len(nums)):
            if nums[i] != 0:
                res[i] = res[i - 1] / nums[i] * prevNum
            else:
                if i + 1 < len(nums):
                    res[i] = self.calProduct(nums[:i] + nums[i + 1:])
                else:
                    res[i] = self.calProduct(nums[:i])
            prevNum = nums[i]
        return res

    def calProduct(self, nums):
        ans = 1
        for i in range(len(nums)):
            ans *= nums[i]
        return ans