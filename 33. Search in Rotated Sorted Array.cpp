/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Subscribe to see which companies asked this question
*/
class Solution {
public:
	int search(vector<int>& nums, int target) {
		if (nums.size() != 0)
		{
			unsigned int first = 0;
			unsigned int last = nums.size() - 1;
			do
			{
				unsigned int mid = (first + last) / 2;
				if (nums[mid] == target) 
					return mid;
					
				if (nums[first] < nums[mid])
					if (nums[first] <= target && target <= nums[mid])
						last = mid - 1;
					else
						first = mid + 1;
				else
					if (nums[mid] < target && target <= nums[last])
						first = mid + 1;
					else
						last = mid - 1;
			} while (first != last + 1);
			return -1;
		}
		else
			return -1;
	}
};