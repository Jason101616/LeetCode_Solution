# Given an N by N grid of integers like the following :

# 0 1 2 0
# 1 3 4 0
# 0 0 5 0
# 0 0 0 1

# Each number denotes number of golds in that position.
# 0 : empty
# Given a starting position (i,j) , find the maximum gold you can collect by moving along the grid.

# - Valid move : up, down, right , left.
# - You cannot go back to the visited position.
# - You cannot go to the empty position.
# - Number of gold collected in the path is simple sum of values along the path.

# Hints:

# This is a Graph searching problem. Can you think of any algorithm for searching problem?
# Try to solve it recursively?

class solution:
    def find_gold(self, grid, i, j):
        self.max_gold = 0
        self.grid = grid
        self.visited = set()
        self.visited.add((i, j))
        self.dfs((i, j), 0)
        return self.max_gold

    def dfs(self, cur_cell, prev_ans):
        next_steps = self.find_possible_next(cur_cell)
        cur_ans = prev_ans + grid[cur_cell[0]][cur_cell[1]]
        if not next_steps:
            if cur_ans > self.max_gold:
                self.max_gold = cur_ans
            return
        self.visited.add(cur_cell)
        for cell in next_steps:
            self.dfs(cell, cur_ans)
        self.visited.remove(cur_cell)
    
    def find_possible_next(self, node):
        # check four directions...