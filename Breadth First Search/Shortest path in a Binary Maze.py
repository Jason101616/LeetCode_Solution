# Given a MxN matrix where each element can either be 0 or 1. We need to find the shortest path between a given source cell to a destination cell. The path can only be created out of a cell if its value is 1.

# Expected time complexity is O(MN).

# For example –

# Input:
# mat[ROW][COL]  = {{1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
#                   {1, 0, 1, 0, 1, 1, 1, 0, 1, 1 },
#                   {1, 1, 1, 0, 1, 1, 0, 1, 0, 1 },
#                   {0, 0, 0, 0, 1, 0, 0, 0, 0, 1 },
#                   {1, 1, 1, 0, 1, 1, 1, 0, 1, 0 },
#                   {1, 0, 1, 1, 1, 1, 0, 1, 0, 0 },
#                   {1, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
#                   {1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
#                   {1, 1, 0, 0, 0, 0, 1, 0, 0, 1 }};
# Source = {0, 0};
# Destination = {3, 4};

# Output:
# Shortest Path is 11

# idea: use BFS to traverse each node
from collections import defaultdict, deque


def find_next(map, node):
    row, col = len(map), len(map[0])
    ret = []
    if node[0] - 1 >= 0 and map[node[0] - 1][node[1]] > 0:
        ret.append((node[0] - 1, node[1]))
    if node[1] - 1 >= 0 and map[node[0]][node[1] - 1] > 0:
        ret.append((node[0], node[1] - 1))
    if node[0] + 1 < row and map[node[0] + 1][node[1]] > 0:
        ret.append((node[0] + 1, node[1]))
    if node[1] + 1 < col and map[node[0]][node[1] + 1] > 0:
        ret.append((node[0], node[1] + 1))
    return ret


def find_shortest_path(mat, start, end):
    if start == end:
        return 0
    visited = set()
    queue = deque()
    visited.add(start)
    queue.append(start)
    cnt = 0
    while queue:
        cur_len = len(queue)
        for i in range(cur_len):
            cur_node = queue.popleft()
            if cur_node == end:
                return cnt
            for next_node in find_next(mat, cur_node):
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)
        cnt += 1


if __name__ == '__main__':
    mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1,
                                            1], [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 1, 0, 1,
                                            0], [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1,
                                            1], [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]]
    start = (0, 0)
    end = (8, 9)
    ans = find_shortest_path(mat, start, end)
    print(ans)