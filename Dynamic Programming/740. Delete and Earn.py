# Given an array nums of integers, you can perform operations on the array.

# In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

# You start with 0 points. Return the maximum number of points you can earn by applying such operations.

# Example 1:
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation: 
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
# Example 2:
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation: 
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
# Note:

# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        num_dict = collections.defaultdict(lambda : 0)
        for num in nums:
            num_dict[num] += 1
        unique_num = sorted(num_dict.keys())
        dp = [0 for _ in range(len(num_dict))]
        dp[0] = num_dict[unique_num[0]] * unique_num[0]

        for i in range(1, len(dp)):
            if unique_num[i - 1] == unique_num[i] - 1:
                if i - 2 >= 0:
                    dp[i] = max(dp[i - 1], dp[i - 2] + num_dict[unique_num[i]] * unique_num[i])
                else:
                    dp[i] = max(dp[i - 1], num_dict[unique_num[i]] * unique_num[i])
            else:
                dp[i] = dp[i - 1] + num_dict[unique_num[i]] * unique_num[i]
        return dp[-1]