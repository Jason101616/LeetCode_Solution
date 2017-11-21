# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


# Idea: let f(k) = Largest product subarray, from index 0 up to k.
# g(k) = Smallest product subarray, from index 0 up to k.
# then:
# f(k) = max( f(k-1) * A[k], A[k], g(k-1) * A[k] )
# g(k) = min( g(k-1) * A[k], A[k], f(k-1) * A[k] )
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        len_nums = len(nums)
        max_list = [0 for _ in range(len_nums)]
        min_list = [0 for _ in range(len_nums)]
        max_list[0], min_list[0] = nums[0], nums[0]
        cur_max = nums[0]
        for i in range(1, len_nums):
            max_list[i] = max(nums[i] * max_list[i - 1],
                              nums[i] * min_list[i - 1], nums[i])
            min_list[i] = min(nums[i] * max_list[i - 1],
                              nums[i] * min_list[i - 1], nums[i])
            cur_max = max(max_list[i], cur_max)
        return cur_max


# optimize space usage:
# Idea: let f(k) = Largest product subarray, from index 0 up to k.
# g(k) = Smallest product subarray, from index 0 up to k.
# then:
# f(k) = max( f(k-1) * A[k], A[k], g(k-1) * A[k] )
# g(k) = min( g(k-1) * A[k], A[k], f(k-1) * A[k] )
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        len_nums = len(nums)
        max_product, min_product = nums[0], nums[0]
        cur_max = nums[0]
        for i in range(1, len_nums):
            tmp_max, tmp_min = max_product, min_product
            max_product = max(nums[i] * tmp_max, nums[i] * tmp_min, nums[i])
            min_product = min(nums[i] * tmp_max, nums[i] * tmp_min, nums[i])
            cur_max = max(max_product, cur_max)
        return cur_max