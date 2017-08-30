/*
	Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
*/

class Solution {
public:
	int longestConsecutive(vector<int>& nums) {
		unordered_map<int, bool> used;
		for (int i = 0; i < nums.size(); i++) {
			used[nums[i]] = false;
		}
		int longest = 0;
		for (int i = 0; i < nums.size(); i++) {
			if (used[nums[i]])
				continue;
			int current_length = 1;
			for (int j = nums[i] + 1; used.find(j) != used.end(); j++) {
				current_length++;
				used[j] = true;
			}
			for (int j = nums[i] - 1; used.find(j) != used.end(); j--) {
				current_length++;
				used[j] = true;
			}
			longest = max(longest, current_length);
		}
		return longest;
	}
};