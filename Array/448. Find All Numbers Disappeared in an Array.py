# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

# idea: traverse two times. Put the number in the nums[number - 1].
# if the number in nums[number - 1] is in correct place, then break.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for index in range(len(nums)):
            while nums[index] != nums[nums[index] - 1]:
                if nums[nums[index] - 1] == nums[index]:
                    break
                # swap nums[index] and nums[nums[index] - 1]
                tmp = nums[index]
                nums[index] = nums[nums[index] - 1]
                nums[tmp - 1] = tmp
        res = []
        for index, val in enumerate(nums):
            if val != index + 1:
                res.append(index + 1)
        return res