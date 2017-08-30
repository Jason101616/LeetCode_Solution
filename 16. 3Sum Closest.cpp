/*
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/


class Solution {
public:
	int threeSumClosest(vector<int>& nums, int target) {
		sort(nums.begin(), nums.end());
		int min_gap = INT_MAX;
		unsigned int current_gap;
		int current_sum;
		int return_sum;
		for (auto i = nums.begin(); i < nums.end() - 2; i++) {
			if (i > nums.begin() && *i == *(i - 1))
				continue;
			auto j = i + 1; auto k = nums.end() - 1;
			while (j < k) {
				current_sum = *i + *j + *k;
				current_gap = abs(current_sum - target);
				if (current_gap == 0)
					return target;
				if (current_gap < min_gap) {
					min_gap = current_gap;
					return_sum = current_sum;
				}
				if (current_sum < target)
					j++;
				else
					k--;
			}
		}
		return return_sum;
	}
};