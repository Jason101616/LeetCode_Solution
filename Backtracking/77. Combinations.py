# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


# idea: similar as permutation, but you can't choose number which index is smaller than the current number
# TLE
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        self.ans = []
        choice = []
        for i in range(n):
            choice.append(i + 1)
        self.find_combine([], choice, k)
        return self.ans

    def find_combine(self, prev_ans, cur_choice, remain_choice_cnt):
        if remain_choice_cnt == 0:
            self.ans.append(prev_ans)
            return
        if not cur_choice:
            return
        len_cur_choice = len(cur_choice)
        for i in range(len_cur_choice):
            self.find_combine(prev_ans + [cur_choice[i]], cur_choice[i + 1:],
                              remain_choice_cnt - 1)
