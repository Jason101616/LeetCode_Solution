/*
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
*/

class Solution {
public:
	void rotate(vector<vector<int>>& matrix) {
		auto n = matrix.size();
		for (auto i = 0; i < n - 1; ++i)
			for (auto j = 0; j < n - 1 - i; ++j)
				swap(matrix[i][j], matrix[n - 1 - j][n - 1 - i]);
		for (auto i = 0; i < n / 2; ++i)
			for (auto j = 0; j < n; ++j)
				swap(matrix[i][j], matrix[n - 1 - i][j]);
	}
};