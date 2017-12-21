# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Solve it without division and in O(n).

# For example, given [1,2,3,4], return [24,12,8,6].

# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

# cur_ans = prev_ans / cur * prev_num
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret_list = copy.deepcopy(nums)
        prev_num = nums[0]
        ret_list[0] = self.cal_product(nums[1:])
        for i in range(1, len(nums)):
            tmp = nums[i]
            if nums[i] != 0:
                ret_list[i] = ret_list[i - 1] / ret_list[i] * prev_num
            else:
                if i + 1 < len(nums):
                    ret_list[i] = self.cal_product(nums[:i] + nums[i + 1:])
                else:
                    ret_list[i] = self.cal_product(nums[:i])
            prev_num = tmp
        return ret_list
    
    def cal_product(self, nums):
        ans = 1
        for i in range(len(nums)):
            ans *= nums[i]
        return ans