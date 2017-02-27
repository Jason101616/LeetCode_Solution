/*
ou are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
*/
class Solution {
public:
	//recursion
	int climbStairs(int n) {
		if (n == 0 || n == 1)
			return 1;
		else
			return climbStairs(n - 1) + climbStairs(n - 2);
	}
	//iteration
	int climbStairs2(int n) {
		int cur = 1; int prev = 0; int temp;
		for (int i = 1; i <= n; ++i) {
			temp = cur;
			cur += prev;
			prev = temp;
		}
		return cur;
	}
	//Fibonacci
	int climbStairs3(int n) {
		const double s = sqrt(5);
		return (pow((1 + s) / 2, n + 1) - pow((1 - s) / 2, n + 1)) / s;
	}
};