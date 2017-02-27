/*
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
*/
class Solution {
public:
	//O(mn)
	void setZeroes(vector<vector<int>>& matrix) {
		int row = matrix.size();
		int col = matrix[0].size();
		vector<vector<int>> temp = matrix;
		for (int i = 0; i < row; i++)
			for (int j = 0; j < col; j++)
				if (temp[i][j] == 0) {
					for (int k = 0; k < row; k++)
						matrix[k][j] = 0;
					for (int k = 0; k < col; k++)
						matrix[i][k] = 0;
				}
	}
	//O(m + n) 
	void setZeroes(vector<vector<int> > &matrix) {
		const size_t m = matrix.size();
		const size_t n = matrix[0].size();
		vector<bool> row(m, false); // 标记该行是否存在0
		vector<bool> col(n, false); // 标记该列是否存在0
		for (size_t i = 0; i < m; ++i) {
			for (size_t j = 0; j < n; ++j) {
				if (matrix[i][j] == 0) {
					row[i] = col[j] = true;
				}
			}
		}
		for (size_t i = 0; i < m; ++i) {
			if (row[i])
				fill(&matrix[i][0], &matrix[i][0] + n, 0);
		}
		for (size_t j = 0; j < n; ++j) {
			if (col[j]) {
				for (size_t i = 0; i < m; ++i) {
					matrix[i][j] = 0;
				}
			}
		}
	}
	//O(1)
	void setZeroes(vector<vector<int> > &matrix) {
		const size_t m = matrix.size();
		const size_t n = matrix[0].size();
		bool row_has_zero = false; // 第一行是否存在0
		bool col_has_zero = false; // 第一列是否存在0
		for (size_t i = 0; i < n; i++)
			if (matrix[0][i] == 0) {
				row_has_zero = true;
				break;
			}
		for (size_t i = 0; i < m; i++)
			if (matrix[i][0] == 0) {
				col_has_zero = true;
				break;
			}
		for (size_t i = 1; i < m; i++)
			for (size_t j = 1; j < n; j++)
				if (matrix[i][j] == 0) {
					matrix[0][j] = 0;
					matrix[i][0] = 0;
				}
		for (size_t i = 1; i < m; i++)
			for (size_t j = 1; j < n; j++)
				if (matrix[i][0] == 0 || matrix[0][j] == 0)
					matrix[i][j] = 0;
		if (row_has_zero)
			for (size_t i = 0; i < n; i++)
				matrix[0][i] = 0;
		if (col_has_zero)
			for (size_t i = 0; i < m; i++)
				matrix[i][0] = 0;
	}
};