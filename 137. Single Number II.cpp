/*
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
*/

class Solution {
public:
	int singleNumber(vector<int>& nums) {
		int size = sizeof(int) * 8;
		int *temp = new int[size];
		fill_n(temp, size, 0);
		for (auto i : nums)
			for (int j = 0; j < size; ++j)
				temp[j] += (i >> j) & 1;
		int res = 0;
		for (int j = 0; j < size; ++j) {
			temp[j] %= 3;
			res += temp[j] << j;
		}
		return res;
	}
};