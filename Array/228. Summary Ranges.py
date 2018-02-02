# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Example 2:
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]

# basic idea: use 2 pointers
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        l, r = 0, 0
        while r < len(nums):
            while r + 1 < len(nums) and nums[r + 1] == nums[r] + 1:
                r += 1
            cur = str(nums[l])
            if r - l >= 1:
                cur += '->' + str(nums[r])
            res.append(cur)
            r += 1
            l = r
        return res

# approach2: binary search
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        l, r = 0, 0
        while r < len(nums):
            r = self.binary_search(nums, l, len(nums) - 1)
            cur = str(nums[l])
            if r - l >= 1:
                cur += '->' + str(nums[r])
            res.append(cur)
            r += 1
            l = r
        return res

    def binary_search(self, nums, l, r):
        while l < r:
            mid = l + (r - l) // 2 + 1
            if nums[mid] - nums[l] == mid - l:
                l = mid
            else:
                r = mid - 1
        return r