# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?


# idea: Same idea as 118. handle the triangle row by row
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        prev_ans = [1, 1]
        for i in range(3, rowIndex + 2):
            cur_ans = [None] * i
            cur_ans[0] = 1
            for j in range(1, i - 1):
                cur_ans[j] = prev_ans[j - 1] + prev_ans[j]
            cur_ans[i - 1] = 1
            prev_ans = cur_ans
        return cur_ans
