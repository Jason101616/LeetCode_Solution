# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# time: O(n)
# space: O(1)
# idea: sort directly

from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cntNums = Counter(nums)
        sortedKeys = sorted(cntNums.keys(), key=lambda x: cntNums[x], reverse=True)
        return sortedKeys[:k]
