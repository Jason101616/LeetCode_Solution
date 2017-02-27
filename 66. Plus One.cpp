/*
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
*/

class Solution {
public:
	vector<int> plusOne(vector<int>& digits) {
		int add = 1;
		for (int i = digits.size() - 1; i >= 0; --i) {
			if (digits[i] + add < 10) {
				digits[i] += add;
				break;
			}
			digits[i] += add;
			add = digits[i] / 10;
			digits[i] %= 10;
			if (i == 0)
				digits.insert(digits.begin(), 1);
		}
		return digits;
	}
};