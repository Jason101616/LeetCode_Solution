/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


*/
class Solution {
public:
	int trap(vector<int>& height) {
		int res = 0;
		int length = height.size();
		int *left = new int[length];
		int *right = new int[length];
		int left_largest = 0;
		for (auto i = 0; i < length; i++) {
			left_largest = max(left_largest, height[i]);
			left[i] = left_largest;
		}
		int right_largest = 0;
		for (auto i = length - 1; i >= 0; i--) {
			right_largest = max(right_largest, height[i]);
			right[i] = right_largest;
		}
		for (auto i = 0; i < length; i++)
			res += min(left[i], right[i]) - height[i];
		return res;
	}
};