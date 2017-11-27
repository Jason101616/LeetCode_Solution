// You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
// elements are subset of nums2. Find all the next greater numbers for nums1's
// elements in the corresponding places of nums2.

// The Next Greater Number of a number x in nums1 is the first greater number to
// its right in nums2. If it does not exist, output -1 for this number.

// Example 1:
// Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
// Output: [-1,3,-1]
// Explanation:
//     For number 4 in the first array, you cannot find the next greater number
//     for it in the second array, so output -1. For number 1 in the first
//     array, the next greater number for it in the second array is 3. For
//     number 2 in the first array, there is no next greater number for it in
//     the second array, so output -1.
// Example 2:
// Input: nums1 = [2,4], nums2 = [1,2,3,4].
// Output: [3,-1]
// Explanation:
//     For number 2 in the first array, the next greater number for it in the
//     second array is 3. For number 4 in the first array, there is no next
//     greater number for it in the second array, so output -1.
// Note:
// All elements in nums1 and nums2 are unique.
// The length of both nums1 and nums2 would not exceed 1000.

// Solution 1: brute force, too easy

// Solution 2: stack + hash map
// http://www.cnblogs.com/grandyang/p/6399855.html
// 建立每个数字和其右边第一个较大数之间的映射，没有的话就是-1。我们遍历原数组中的所有数字，如果此时栈不为空，且栈顶元素小于当前数字，说明当前数字就是栈顶元素的右边第一个较大数，那么建立二者的映射，并且去除当前栈顶元素，最后将当前遍历到的数字压入栈。当所有数字都建立了映射，那么最后我们可以直接通过哈希表快速的找到子集合中数字的右边较大值

class Solution {
  public:
    vector<int> nextGreaterElement(vector<int> &findNums, vector<int> &nums) {
        vector<int> res;
        stack<int> st;
        unordered_map<int, int> m;
        for (int num : nums) {
            while (!st.empty() && st.top() < num) {
                m[st.top()] = num;
                st.pop();
            }
            st.push(num);
        }
        for (int num : findNums) {
            res.push_back(m.count(num) ? m[num] : -1);
        }
        return res;
    }
};