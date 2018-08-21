# Given an integer matrix, find the length of the longest increasing path.

# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

# Example 1:

# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].

# Example 2:

# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


# idea: make each cell as the starting point, use DFS to calculate the longest increasing path starting from this point.
# maintain a dp. But this dp is not optimal. We should update the dp during the dfs, not after dfs.
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        self.matrix = matrix
        self.row, self.col = len(matrix), len(matrix[0])
        self.ans = []
        self.dp = [[0 for _ in range(self.col)] for __ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.cur_ans = []
                self.dfs((i, j), 1)
                cur_ans = max(self.cur_ans)
                self.ans.append(cur_ans)
                self.dp[i][j] = cur_ans
        return max(self.ans)

    def dfs(self, cur_cell, cur_length):
        if self.dp[cur_cell[0]][cur_cell[1]]:
            self.cur_ans.append(cur_length + self.dp[cur_cell[0]][cur_cell[1]]
                                - 1)
            return
        possible_next_cells = self.find_next(cur_cell)
        if not possible_next_cells:
            self.cur_ans.append(cur_length)
            return
        for cell in possible_next_cells:
            self.dfs(cell, cur_length + 1)

    def find_next(self, cell):
        cur_val = self.matrix[cell[0]][cell[1]]
        poss_next = []
        if cell[0] - 1 >= 0 and self.matrix[cell[0] - 1][cell[1]] > cur_val:
            poss_next.append((cell[0] - 1, cell[1]))
        if cell[0] + 1 < self.row and self.matrix[cell[0]
                                                  + 1][cell[1]] > cur_val:
            poss_next.append((cell[0] + 1, cell[1]))
        if cell[1] - 1 >= 0 and self.matrix[cell[0]][cell[1] - 1] > cur_val:
            poss_next.append((cell[0], cell[1] - 1))
        if cell[1] + 1 < self.col and self.matrix[cell[0]][cell[1]
                                                           + 1] > cur_val:
            poss_next.append((cell[0], cell[1] + 1))
        return poss_next


# Solution 2: update a dp array during the dfs. (C++)
class Solution {
public:
    vector < vector < int >> dirs = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
    int


longestIncreasingPath(vector < vector < int >> & matrix)
{
if (matrix.empty() | | matrix[0].empty())
return 0;
int
res = 1, m = matrix.size(), n = matrix[0].size();
vector < vector < int >> dp(m, vector < int > (n, 0));
for (int i = 0; i < m; ++i) {
for (int j = 0; j < n; ++j) {
res = max(res, dfs(matrix, dp, i, j));
}
}
return res;
}
int
dfs(vector < vector < int >> & matrix, vector < vector < int >> & dp, int
i, int
j) {
if (dp[i][j]) return dp[i][j];
int
mx = 1, m = matrix.size(), n = matrix[0].size();
for (auto a: dirs) {
    int x = i + a[0], y = j + a[1];
if (x < 0 | | x >= m | | y < 0 | | y >= n | | matrix[x][y] <= matrix[i][j])
continue;
int
len = 1 + dfs(matrix, dp, x, y);
mx = max(mx, len);
}
dp[i][j] = mx;
return mx;
}
};
