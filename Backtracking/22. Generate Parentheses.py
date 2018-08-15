# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# Recursive:
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(res, "", n, n)
        return res

    def helper(self, res, curRes, leftRemain, rightRemain):
        if leftRemain == 0 and rightRemain == 0:
            res.append(curRes)
            return

        if leftRemain == rightRemain:
            self.helper(res, curRes + '(', leftRemain - 1, rightRemain)
        else:
            if leftRemain > 0:
                self.helper(res, curRes + '(', leftRemain - 1, rightRemain)
            self.helper(res, curRes + ')', leftRemain, rightRemain - 1)

# DP:
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n, {})

    def helper(self, leftRemain, rightRemain, memo):
        if (leftRemain, rightRemain) in memo:
            return memo[(leftRemain, rightRemain)]

        if leftRemain == 0 and rightRemain == 0:
            return ['']

        if leftRemain == rightRemain:
            tmpRes = self.helper(leftRemain - 1, rightRemain, memo)
            res = ['(' + tmp for tmp in tmpRes]
            memo[(leftRemain, rightRemain)] = res
            return res
        else:
            res = []
            if leftRemain > 0:
                tmpRes = self.helper(leftRemain - 1, rightRemain, memo)
                res = ['(' + tmp for tmp in tmpRes]
            tmpRes = self.helper(leftRemain, rightRemain - 1, memo)
            res2 = [')' + tmp for tmp in tmpRes]
            res.extend(res2)
            memo[(leftRemain, rightRemain)] = res
            return res
