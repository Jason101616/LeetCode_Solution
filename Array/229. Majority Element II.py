# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt0, cnt1, candidate0, candidate1 = 0, 0, None, None
        for num in nums:
            if num == candidate0:
                cnt0 += 1
            elif num == candidate1:
                cnt1 += 1
            elif cnt0 == 0:
                candidate0, cnt0 = num, 1
            elif cnt1 == 0:
                candidate1, cnt1 = num, 1
            else:
                cnt0 -= 1
                cnt1 -= 1
        res = []
        for can in [candidate0, candidate1]:
            if can != None and nums.count(can) > (len(nums) // 3):
                res.append(can)
        return res
