# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# time: O(nlogn)
# space: O(n)
# idea: simple priority queue

import Queue


class number:
    def __init__(self, num):
        self.num = num
        self.freq = 1

    def __lt__(self, other):
        return self.freq > other.freq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_dict = {}
        q = Queue.PriorityQueue()
        for num in nums:
            if num not in num_dict:
                new_num = number(num)
                num_dict[num] = new_num
            else:
                num_dict[num].freq += 1
        for num in num_dict:
            q.put(num_dict[num])
        ret_list = []
        for i in range(k):
            ret_list.append(q.get().num)
        return ret_list
