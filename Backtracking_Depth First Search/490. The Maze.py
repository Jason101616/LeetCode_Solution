# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
#
# Example 1
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
#
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
#
# Example 2
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
#
# Output: false
# Explanation: There is no way for the ball to stop at the destination.
#
# Note:
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        row, col = len(maze), len(maze[0])
        visited = [[False for _ in range(col)] for __ in range(row)]
        visited[start[0]][start[1]] = True
        return self.dfs(maze, start, destination, visited)

    def dfs(self, maze, curPoint, destination, visited):
        if curPoint == destination:
            return True
        for nextPoint in self.nextStepHelper(maze, curPoint, visited):
            if not visited[nextPoint[0]][nextPoint[1]]:
                visited[nextPoint[0]][nextPoint[1]] = True
                if self.dfs(maze, nextPoint, destination, visited):
                    return True
        return False

    def nextStepHelper(self, maze, curPoint, visited):
        res = []
        row, col = len(maze), len(maze[0])
        findAns = False
        for i in range(curPoint[1] + 1, col):
            if maze[curPoint[0]][i] == 1:
                findAns = True
                if not visited[curPoint[0]][i - 1]:
                    res.append([curPoint[0], i - 1])
                break
        if not findAns and not visited[curPoint[0]][col - 1]:
            res.append([curPoint[0], col - 1])

        findAns = False
        for i in range(curPoint[1] - 1, -1, -1):
            if maze[curPoint[0]][i] == 1:
                findAns = True
                if not visited[curPoint[0]][i + 1]:
                    res.append([curPoint[0], i + 1])
                break
        if not findAns and not visited[curPoint[0]][0]:
            res.append([curPoint[0], 0])

        findAns = False
        for i in range(curPoint[0] + 1, row):
            if maze[i][curPoint[1]] == 1:
                findAns = True
                if not visited[i - 1][curPoint[1]]:
                    res.append([i - 1, curPoint[1]])
                break
        if not findAns and not visited[row - 1][curPoint[1]]:
            res.append([row - 1, curPoint[1]])

        findAns = False
        for i in range(curPoint[0] - 1, -1, -1):
            if maze[i][curPoint[1]] == 1:
                findAns = True
                if not visited[i + 1][curPoint[1]]:
                    res.append([i + 1, curPoint[1]])
                break
        if not findAns and not visited[0][curPoint[1]]:
            res.append([0, curPoint[1]])

        return res