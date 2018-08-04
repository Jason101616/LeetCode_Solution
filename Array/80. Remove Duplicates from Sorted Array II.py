# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

# this method can support any number duplicates, just change dup_allow
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dup_allow = 2
        left = 1
        dup_cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                dup_cnt = 1
                nums[left] = nums[i]
                left += 1
            else:
                dup_cnt += 1
                if dup_cnt <= dup_allow:
                    nums[left] = nums[i]
                    left += 1
        return left
