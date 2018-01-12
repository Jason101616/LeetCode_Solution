# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + '->' + str(upper)]
        res = []
        if nums[0] != lower:
            if nums[0] - 1 == lower:
                res.append(str(lower))
            else:
                res.append(str(lower) + '->' + str(nums[0] - 1))
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] != (nums[i - 1] + 1):
                if nums[i - 1] + 1 == nums[i] - 1:
                    res.append(str(nums[i - 1] + 1))
                else:
                    res.append(str(nums[i - 1] + 1) + '->' + str(nums[i] - 1))
        if nums[-1] != upper:
            if nums[-1] + 1 == upper:
                res.append(str(upper))
            else:
                res.append(str(nums[-1] + 1) + '->' + str(upper))
        return res