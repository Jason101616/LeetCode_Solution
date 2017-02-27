/*
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
*/
//Solution 1: invoke nextPermutation k - 1 times (Bad solution)
class Solution {
public:
	void nextPermutation(vector<int>& nums) {
		auto i = nums.rbegin();
		for (; i != nums.rend() - 1; i++)
			if (!(*i <= *(i + 1))) {
				auto j = nums.rbegin();
				for (; j != (i + 1); j++)
					if (*j > *(i + 1)) {
						swap(*j, *(i + 1));
						break;
					}
				reverse(nums.rbegin(), i + 1);
				break;
			}
		if (i == nums.rend() - 1)
			reverse(nums.begin(), nums.end());
	}

	string getPermutation(int n, int k) {
		vector<int> temp;
		for (auto i = 1; i <= n; i++)
			temp.push_back(i);
		for (auto i = 0; i < k - 1; i++)
			nextPermutation(temp);
		string res;
		for (auto i = 0; i < n; i++)
			res += to_string(temp[i]);
		return res;
	}
};
//Solution 2: Cantor coding
class Solution {
public:
	string getPermutation(int n, int k) {
		string temp;
		for (int i = 1; i <= n; i++)
			temp += to_string(i);
		string res;
		k--;
		for (int i = n - 1; i >= 0; --i) {
			int a = k / factorial(i);
			res.push_back(temp[a]);
			temp.erase(a, 1);
			k %= factorial(i);
		}
		return res;
	}
private:
	int factorial(int n) {
		int res = 1;
		for (int i = 1; i <= n; ++i)
			res *= i;
		return res;
	}
};