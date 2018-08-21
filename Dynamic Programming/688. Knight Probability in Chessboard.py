# On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
#
# A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
#
#
# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
#
# The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.
#
# Example:
# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.
# Note:
# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.

# time: O(n ^ 2 * k), dp

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        memo = {}
        return 1.0 * self.dfs(N, K, r, c, 0, memo) / pow(8, K)

    def dfs(self, N, K, r, c, curMov, memo):
        if (r, c, K - curMov) in memo:
            return memo[(r, c, K - curMov)]
        if not self.isInChessboard(N, r, c):
            return 0
        if curMov == K:
            return 1
        moveDirections = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
        res = 0
        for dirc in moveDirections:
            res += self.dfs(N, K, r + dirc[0], c + dirc[1], curMov + 1, memo)
        memo[(r, c, K - curMov)] = res
        return res

    def isInChessboard(self, N, r, c):
        if r >= N or r < 0:
            return False
        if c >= N or c < 0:
            return False
        return True
