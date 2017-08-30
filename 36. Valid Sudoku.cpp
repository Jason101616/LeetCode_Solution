/*
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A partially filled sudoku which is valid.
*/
class Solution {
public:
	bool isValidSudoku(vector<vector<char>>& board) {
		bool is_filled[9];
		int i, j;
		//check row
		for (i = 0; i < 9; i++) {
			fill(is_filled, is_filled + 9, false);
			for (j = 0; j < 9; j++) {
				if (board[i][j] == '.')
					continue;
				if (is_filled[board[i][j] - '1'])
					return false;

				if (!is_filled[board[i][j] - '1'])
					is_filled[board[i][j] - '1'] = true;
			}
		}

		//check column
		for (j = 0; j < 9; j++) {
			fill(is_filled, is_filled + 9, false);
			for (i = 0; i < 9; i++) {
				if (board[i][j] == '.')
					continue;
				if (is_filled[board[i][j] - '1'])
					return false;
				if (!is_filled[board[i][j] - '1'])
					is_filled[board[i][j] - '1'] = true;
			}
		}

		//check sub-boxes
		for (i = 0; i < 3; i++)
			for (j = 0; j < 3; j++) {
				fill(is_filled, is_filled + 9, false);
				for (int row = i * 3; row < i * 3 + 3; row++)
					for (int col = j * 3; col < j * 3 + 3; col++) {
						if (board[row][col] == '.')
							continue;
						if (is_filled[board[row][col] - '1'])
							return false;
						if (!is_filled[board[row][col] - '1'])
							is_filled[board[row][col] - '1'] = true;
					}
			}
		return true;
	}
};