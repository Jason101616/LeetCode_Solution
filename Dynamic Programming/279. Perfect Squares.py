# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.


# idea: # use dp to calculate the number
# dp[n] = min(1 + dp[n - i]) where i is the square number smaller than n
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # generate the list of square numbers
        square_num = 100
        self.square_list = [None for _ in range(square_num)]
        for i in range(square_num):
            self.square_list[i] = (i + 1) * (i + 1)
        # use dp to calculate the number
        # dp[n] = min(1 + dp[n - i]) where i is the square number smaller than n
        dp = [None for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            smaller_squares = self.find_smaller_squares(i, 0, square_num - 1)
            len_smaller_squares = len(smaller_squares)
            tmp_ans = [None for _ in range(len_smaller_squares)]
            for j in range(len_smaller_squares):
                tmp_ans[j] = 1 + dp[i - smaller_squares[j]]
            dp[i] = min(tmp_ans)

        return dp[n]

    def find_smaller_squares(self, num, left, right):
        if left >= right:
            if num >= self.square_list[left]:
                return self.square_list[:left + 1]
            else:
                return self.square_list[:left]
        middle = (left + right) // 2
        if self.square_list[middle] == num:
            return self.square_list[:middle + 1]
        elif self.square_list[middle] > num:
            return self.find_smaller_squares(num, left, middle - 1)
        else:
            return self.find_smaller_squares(num, middle + 1, right)
