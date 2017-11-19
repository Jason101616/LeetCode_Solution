# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


# Solution 1:
# idea: use backtracking. For every num in the nums, we can make it as the first number in the answer
# then modify the current nums and go to the next phase.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.ans = []
        self.find_permute([], nums)
        return self.ans

    def find_permute(self, prev_ans, cur_nums):
        if not cur_nums:
            self.ans.append(prev_ans)
            return
        len_cur_nums = len(cur_nums)
        for i in range(len_cur_nums):
            cur_ans = prev_ans + [cur_nums[i]]
            self.find_permute(cur_ans, cur_nums[:i] + cur_nums[i + 1:])


# Solution 2
# idea: backtracing. Swap numbers and DFS.
import copy


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret_list = []
        self.per(nums, ret_list, 0)
        return ret_list

    def per(self, nums, ret_list, index):
        if index >= len(nums):
            ret_list.append(copy.deepcopy(nums))
            return

        for i in range(index, len(nums)):
            if i != index:
                self.swap(nums, index, i)
            self.per(nums, ret_list, index + 1)
            if i != index:
                self.swap(nums, index, i)

    def swap(self, nums, i1, i2):
        tmp = nums[i1]
        nums[i1] = nums[i2]
        nums[i2] = tmp
