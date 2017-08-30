/*
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
*/

class Solution {
public:
	int candy(vector<int>& ratings) {
		int size = ratings.size();
		vector<int> temp(size, 1);
		for (int i = 1; i < size; ++i)
			if (ratings[i] > ratings[i - 1])
				temp[i] = temp[i - 1] + 1;
		for (int i = size - 2; i >= 0; --i)
			if (ratings[i] > ratings[i + 1])
				temp[i] = max(temp[i], temp[i + 1] + 1);
		int res = 0;
		for (auto i = 0; i < size; ++i)
			res += temp[i];
		return res;
	}
};