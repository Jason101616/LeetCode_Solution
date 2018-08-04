# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

# solution 1: quick select algorithm
# time: average O(n). worst time O(n^2)
# idea: 把比某个数大的数都放在该数的左边。然后一步步缩小范围。

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos == k - 1:
                return nums[pos]
            if pos > k - 1:
                right = pos - 1
            else:
                left = pos + 1

    def partition(self, nums, left, right):
        pivot_pos, pivot_val = left, nums[left]
        for i in range(left + 1, right + 1):
            if nums[i] > pivot_val:
                pivot_pos += 1
                if pivot_pos != i:
                    nums[pivot_pos], nums[i] = nums[i], nums[pivot_pos]
        nums[left] = nums[pivot_pos]
        nums[pivot_pos] = pivot_val
        return pivot_pos


# solution 2: use heap
# time: O(N * log(k))
import queue  # python 3


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = queue.PriorityQueue()
        for num in nums:
            q.put(num)
            if q.qsize() > k:
                q.get()
        return q.get()
