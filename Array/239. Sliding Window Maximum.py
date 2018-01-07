# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].

# Note:
# You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

# Follow up:
# Could you solve it in linear time?

# Solution 1: use PriorityQueue
# time: O(nlogn)
# each time, store (nums[i], i) in PriorityQueue. Each time if the head of the PriorityQueue needed to be evicted, then evicted it and then insert
# the new number into the PriorityQueue and retreive the first element of the PriorityQueue.
try:
    from queue import PriorityQueue
except:
    from Queue import PriorityQueue


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []
        ans = []
        q = PriorityQueue()
        for i in range(k):
            q.put((-nums[i], i))
        ans.append(-q.queue[0][0])
        for i in range(k, len(nums)):
            while q.qsize() > 0 and q.queue[0][1] < i + 1 - k:
                q.get()
            q.put((-nums[i], i))
            ans.append(-q.queue[0][0])
        return ans


# Solution 2: use deque
# time: O(n)
# idea: 滑动窗口的最大值总是保存在队列首部，队列里面的数据总是从大到小排列。当遇到比当前滑动窗口最大值更大的值时，则将队列清空，并将新的最大值插入到队列中。如果遇到的值比当前最大值小，则直接插入到队列尾部。每次移动的时候需要判断当前的最大值是否在有效范围，如果不在，则需要将其从队列中删除。由于每个元素最多进队和出队各一次，因此该算法时间复杂度为O(N)。

from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return []
        deque_window = deque()
        ret_list = []
        for i in range(k):
            while deque_window and nums[i] >= nums[deque_window[len(
                    deque_window) - 1]]:
                deque_window.pop()
            deque_window.append(i)

        for i in range(k, len(nums)):
            ret_list.append(nums[deque_window[0]])
            while deque_window and nums[i] >= nums[deque_window[len(
                    deque_window) - 1]]:
                deque_window.pop()
            while deque_window and deque_window[0] < i - k + 1:
                deque_window.popleft()
            deque_window.append(i)
        ret_list.append(nums[deque_window[0]])
        return ret_list
