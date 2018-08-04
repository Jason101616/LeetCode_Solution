# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

# BFS. EZ.
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        INF = 2147483647
        q = collections.deque()
        row, col = len(rooms), len(rooms[0])
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    q.append((i, j))
        distance = 0
        while q:
            curLen = len(q)
            for i in range(curLen):
                x, y = q.popleft()
                if rooms[x][y] == INF:
                    rooms[x][y] = distance
                if x + 1 < row and rooms[x + 1][y] == INF:
                    q.append((x + 1, y))
                if x - 1 >= 0 and rooms[x - 1][y] == INF:
                    q.append((x - 1, y))
                if y + 1 < col and rooms[x][y + 1] == INF:
                    q.append((x, y + 1))
                if y - 1 >= 0 and rooms[x][y - 1] == INF:
                    q.append((x, y - 1))
            distance += 1
