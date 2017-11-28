# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


# same idea as 54. Spital Matrix
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[None for _ in range(n)] for __ in range(n)]
        start = [0, 0]
        cnt = 0
        while cnt != n * n:
            while start[1] < n and not ans[start[0]][start[1]]:
                cnt += 1
                ans[start[0]][start[1]] = cnt
                start[1] += 1
            start[0] += 1
            start[1] -= 1
            while start[0] < n and not ans[start[0]][start[1]]:
                cnt += 1
                ans[start[0]][start[1]] = cnt
                start[0] += 1
            start[0] -= 1
            start[1] -= 1
            while start[1] >= 0 and not ans[start[0]][start[1]]:
                cnt += 1
                ans[start[0]][start[1]] = cnt
                start[1] -= 1
            start[0] -= 1
            start[1] += 1
            while start[0] >= 0 and not ans[start[0]][start[1]]:
                cnt += 1
                ans[start[0]][start[1]] = cnt
                start[0] -= 1
            start[0] += 1
            start[1] += 1
        return ans