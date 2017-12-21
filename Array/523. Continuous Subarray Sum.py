# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
# Note:
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

# idea: use a dictionary to maintain the mapping between sum and index
# time: O(n)
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum_index_map = {0: -1}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if k != 0:
                cur_sum %= k
            if cur_sum not in sum_index_map:
                sum_index_map[cur_sum] = i
            else:
                if i - sum_index_map[cur_sum]> 1:
                    return True
        return False

# Solution 2: brute force

public class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int[] sum = new int[nums.length];
        sum[0] = nums[0];
        for (int i = 1; i < nums.length; i++)
            sum[i] = sum[i - 1] + nums[i];
        for (int start = 0; start < nums.length - 1; start++) {
            for (int end = start + 1; end < nums.length; end++) {
                int summ = sum[end] - sum[start] + nums[start];
                if (summ == k || (k != 0 && summ % k == 0))
                    return true;
            }
        }
        return false;
    }
}