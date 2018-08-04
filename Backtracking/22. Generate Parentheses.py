# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


# idea: generate the answer recursively, using backtracking. Also should discuss different condition
# (1) l_remain == 0 and r_remain == 0 return current answer
# (2) l_remain < r_remain and l_remain > 0, can have different direction to go
# (3) l_remain == r_remain and both > 0, can only choose left
# (4) l_remain == 0 and r_remain > 0, can only choose right
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        self.ans = []
        self.gen_par("", n, n)
        return self.ans

    def gen_par(self, cur_ans, l_remain, r_remain):
        if l_remain == 0 and r_remain == 0:
            self.ans.append(cur_ans)
            return
        if l_remain < r_remain and l_remain > 0:
            self.gen_par(cur_ans + '(', l_remain - 1, r_remain)
            self.gen_par(cur_ans + ')', l_remain, r_remain - 1)
        elif l_remain == r_remain:
            self.gen_par(cur_ans + '(', l_remain - 1, r_remain)
        elif l_remain == 0:
            self.gen_par(cur_ans + ')', l_remain, r_remain - 1)
