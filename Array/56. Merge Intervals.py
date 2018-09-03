# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# idea: start from the left interval, if the end of a interval is less than or equal to the start of the next interval,
# then merge them and put them into a new list.
# time: O(n * logn)
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x.start, x.end))
        mergeIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if self.isOverlap(intervals[i], mergeIntervals[-1]):
                mergeIntervals[-1].end = max(intervals[i].end, mergeIntervals[-1].end)
            else:
                mergeIntervals.append(intervals[i])
        return mergeIntervals

    def isOverlap(self, i1, i2):
        return i2.end >= i1.start
