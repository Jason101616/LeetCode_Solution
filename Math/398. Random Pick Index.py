# Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.

# Example:

# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);

# // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);

# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);

# Reservoir Sampling problem
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt, res = -1, None
        for index, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                rand_num = random.randint(0, cnt)
                if rand_num == 0:
                    res = index
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
