# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X

# idea: use BFS, start from the node in the edge
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        q = collections.deque()
        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for i in range(n):
            if board[0][i] == 'O':
                visited.add((0, i))
                q.append((0, i))
        for i in range(n):
            if board[m - 1][i] == 'O':
                visited.add((m - 1, i))
                q.append((m - 1, i))
        for i in range(m):
            if board[i][0] == 'O':
                visited.add((i, 0))
                q.append((i, 0))
        for i in range(m):
            if board[i][n - 1] == 'O':
                visited.add((i, n - 1))
                q.append((i, n - 1))
        while q:
            cur_node = q.popleft()
            for direction in directions:
                new_x, new_y = cur_node[0] + direction[0], cur_node[1] + direction[1]
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and board[new_x][new_y] == 'O' and (
                new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    q.append((new_x, new_y))
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
