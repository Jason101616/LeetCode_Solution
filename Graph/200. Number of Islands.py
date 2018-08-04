# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011
# Answer: 3


# Time:  O(m * n)
# Space: O(m * n)
# idea: for each node use bfs, count the connected area of the graph


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visited = [[False for i in range(col)] for j in range(row)]
        cnt = 0
        for i in range(row):
            for j in range(col):
                cnt += self.bfs(i, j, grid, visited, row, col)
        return cnt

    def bfs(self, sx, sy, grid, visited, row, col):
        # is sea or has been visited
        if not int(grid[sx][sy]) or visited[sx][sy]:
            return 0
        queue = collections.deque()
        visited[sx][sy] = True
        queue.append((sx, sy))
        while queue:
            cx, cy = queue.popleft()
            for nx, ny in [[cx, cy + 1], [cx + 1, cy], [cx - 1, cy], [cx, cy - 1]]:
                if not (nx < 0 or nx >= row or ny < 0 or ny >= col) and not visited[nx][ny] and int(grid[nx][ny]):
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        return 1


# Time:  O(m * n)
# Space: O(m * n)
# idea: for each node use dfs, count the connected area of the graph
import collections


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visited = [[False for i in range(col)] for j in range(row)]
        cnt = 0
        for i in range(row):
            for j in range(col):
                cnt += self.dfs(i, j, grid, visited, row, col)
        return cnt

    def dfs(self, sx, sy, grid, visited, row, col):
        # is sea or has been visited
        if not int(grid[sx][sy]) or visited[sx][sy]:
            return 0
        visited[sx][sy] = True
        for nx, ny in [[sx, sy + 1], [sx + 1, sy], [sx - 1, sy], [sx, sy - 1]]:
            if not (nx < 0 or nx >= row or ny < 0 or ny >= col) and not visited[nx][ny] and int(grid[nx][ny]):
                self.dfs(nx, ny, grid, visited, row, col)
        return 1
