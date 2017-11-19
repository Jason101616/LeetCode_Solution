# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# For example, given nums = [-2, 0, 1, 3], and target = 2.

# Return 2. Because there are two triplets which sums are less than 2:

# [-2, 0, 1]
# [-2, 0, 3]
# Follow up:
# Could you solve it in O(n2) runtime?


# idea: two pointers. easy.
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ret = 0
        len_nums = len(nums)
        for i in range(len_nums - 2):
            left, right = i + 1, len_nums - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] >= target:
                    right -= 1
                    continue
                ret += (right - left)
                left += 1
        return ret
