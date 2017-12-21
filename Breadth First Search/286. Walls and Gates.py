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

# start BFS from all gates
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        can_visit = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        queue = collections.deque()
        row, col = len(rooms), len(rooms[0])
        # push all gates into queue
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        # use BFS to calculate the distance
        visited = [[False for _ in range(col)] for __ in range(row)]
        distance = 0
        while queue:
            distance += 1
            cur_len = len(queue)
            for i in range(cur_len):
                cur_point = queue.popleft()
                x_pos, y_pos = cur_point[0], cur_point[1]
                for direction in can_visit:
                    new_x_pos, new_y_pos = x_pos + direction[0], y_pos + direction[1]
                    # prune some invalid edge case
                    if new_x_pos < 0 or new_x_pos >= row or new_y_pos < 0 or new_y_pos >= col or rooms[new_x_pos][new_y_pos] == -1 or visited[new_x_pos][new_y_pos]:
                        continue
                    if rooms[new_x_pos][new_y_pos] > distance:
                        rooms[new_x_pos][new_y_pos] = distance
                    visited[new_x_pos][new_y_pos] = True
                    queue.append([new_x_pos, new_y_pos])