/*
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

Subscribe to see which companies asked this question
*/
class Solution {
public:
	bool search(vector<int>& nums, int target) {
		if (nums.size() != 0)
		{
			unsigned int first = 0;
			unsigned int last = nums.size() - 1;
			do
			{
				unsigned int mid = (first + last) / 2;
				if (nums[mid] == target)
					return true;

				if (nums[first] < nums[mid])
					if (nums[first] <= target && target <= nums[mid])
						last = mid - 1;
					else
						first = mid + 1;
				else if (nums[first] == nums[mid])
					first++;
				else
					if (nums[mid] < target && target <= nums[last])
						first = mid + 1;
					else
						last = mid - 1;
			} while (first != last + 1);
			return false;
		}
		else
			return false;
	}
};