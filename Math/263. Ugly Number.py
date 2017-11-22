# idea: recursively divide those three prime factors
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        find_ans = False
        for i in [2, 3, 5]:
            if not find_ans:
                quotient = num // i
                if quotient * i == num:
                    find_ans = True
                    return self.isUgly(quotient)
        return False