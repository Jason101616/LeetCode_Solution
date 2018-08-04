# You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
# You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

# You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

# You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

# Example 1:
# Input: 
# [
#  [1,2,3],
#  [0,0,4],
#  [7,6,5]
# ]
# Output: 6
# Example 2:
# Input: 
# [
#  [1,2,3],
#  [0,0,0],
#  [7,6,5]
# ]
# Output: -1
# Example 3:
# Input: 
# [
#  [2,3,4],
#  [0,0,5],
#  [8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
# Hint: size of the given matrix will not exceed 50x50.


# Time:  O(row * row * col * col)
# Space: O(row * col)
# idea: Sort the node and perform BFS from start node to end node. Add up the path.
import collections


class Solution(object):
    def cutOffTree(self, G):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not G or not G[0] or not G[0][0]:
            return -1
        graph = []
        row, col = len(G), len(G[0])
        for i in range(row):
            for j in range(col):
                if G[i][j] > 1:
                    graph.append((G[i][j], i, j))
        graph.sort()
        step, sx, sy = 0, 0, 0
        for h, x, y in graph:
            length = self.BFS(G, sx, sy, x, y)
            if length == -1:
                return -1
            step += length
            sx, sy, G[x][y] = x, y, 1
        return step

    def BFS(self, G, sx, sy, tx, ty):
        row, col = len(G), len(G[0])
        # visited = [[False] * col] * row
        visited = [[False for i in range(col)] for j in range(row)]
        queue = collections.deque()
        visited[sx][sy] = True
        queue.append((sx, sy))
        length = -1
        while queue:
            length += 1
            size = len(queue)
            for _ in range(size):
                cx, cy = queue.popleft()
                if cx == tx and cy == ty:
                    return length
                for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy - 1), (cx, cy + 1)]:
                    if nx < 0 or nx >= row or ny < 0 or ny >= col or G[nx][ny] == 0 or visited[nx][ny]:
                        continue
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        return -1
