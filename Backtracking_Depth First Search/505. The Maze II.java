// There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

// Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

// The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

// Example 1

// Input 1: a maze represented by a 2D array

// 0 0 1 0 0
// 0 0 0 0 0
// 0 0 0 1 0
// 1 1 0 1 1
// 0 0 0 0 0

// Input 2: start coordinate (rowStart, colStart) = (0, 4)
// Input 3: destination coordinate (rowDest, colDest) = (4, 4)

// Output: 12
// Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
//              The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

// Example 2

// Input 1: a maze represented by a 2D array

// 0 0 1 0 0
// 0 0 0 0 0
// 0 0 0 1 0
// 1 1 0 1 1
// 0 0 0 0 0

// Input 2: start coordinate (rowStart, colStart) = (0, 4)
// Input 3: destination coordinate (rowDest, colDest) = (3, 2)

// Output: -1
// Explanation: There is no way for the ball to stop at the destination.

// Note:
// There is only one ball and one destination in the maze.
// Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
// The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
// The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

class Solution {
    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        int res = Integer.MAX_VALUE;
        int m = maze.length;
        int n = maze[0].length;

        int[][] move = new int[][] {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
        Queue<int[]> queue = new LinkedList<>();
        int[][] length = new int[m][n];
        for (int i = 0; i < m * n; i++)
            length[i / n][i % n] = Integer.MAX_VALUE;
        // Initial distance here.
        queue.offer(new int[] {start[0], start[1], 0});
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            if (length[cur[0]][cur[1]] <= cur[2]) // pruning here
                continue;
            length[cur[0]][cur[1]] = cur[2];
            if (cur[0] == destination[0] && cur[1] == destination[1]) {
                res = Math.min(cur[2], res);
            }

            for (int[] mo : move) {
                int x = cur[0], y = cur[1];
                int d = cur[2];
                while (x >= 0 && x < m && y >= 0 && y < n && maze[x][y] == 0) {
                    x += mo[0];
                    y += mo[1];
                    d++;
                }
                d--;
                // Back to validate point.
                x -= mo[0];
                y -= mo[1];

                // Adding new start point. d is distance.
                queue.offer(new int[] {x, y, d});
            }
        }
        return res == Integer.MAX_VALUE ? -1 : res;
    }
}

class Solution {
    static final int[] DIRS = {0, 1, 0, -1, 0};
    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        int[][] dist = new int[maze.length][maze[0].length];
        dist[start[0]][start[1]] = 1;
        dfs(start[0], start[1], destination, maze, dist);
        return dist[destination[0]][destination[1]] - 1;
    }
    void dfs(int row, int col, int[] dest, int[][] maze, int[][] dist) {
        if (row == dest[0] && col == dest[1]) return;
        int m = maze.length, n = maze[0].length;
        for (int d = 0; d < 4; ++d) {
            int i = row, j = col, p = DIRS[d], q = DIRS[d + 1], len = dist[row][col];
            while (i + p >= 0 && i + p < m && j + q >= 0 && j + q < n && maze[i + p][j + q] == 0) {
                i += p;
                j += q;
                len++;
            }
            if (dist[i][j] > 0 && len >= dist[i][j]) continue;
            dist[i][j] = len;
            dfs(i, j, dest, maze, dist);
        }
    }
}