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


# Solution 2:
# idea: swap with the first item every time, until cannot swap
# time: O(n!) n factorial
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ans = []
        self.find_permutation(ans, nums, 0)
        return ans
    
    def find_permutation(self, ans, nums, start):
        if start == len(nums) - 1:
            ans.append(copy.deepcopy(nums))
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            self.find_permutation(ans, nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]

# Solution 3:
# backtracking, mark whether each element has been used
class Solution(object):
    def permute(self, nums):
        if not nums:
            return []
        res = []
        cur = []
        used = [False for _ in range(len(nums))]
        self.find_permutation(res, cur, nums, used)
        return res

    def find_permutation(self, res, cur, nums, used):
        if len(cur) == len(nums):
            res.append(list(cur))
            return
        for i in range(len(nums)):
            if not used[i]:
                cur.append(nums[i])
                used[i] = True
                self.find_permutation(res, cur, nums, used)
                used[i] = False
                cur.pop()
