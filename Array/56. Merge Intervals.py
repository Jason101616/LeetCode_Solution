# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# idea: start from the left interval, if the end of a interval is less than or equal to than the start of the next interval,
# then merge them and put them into a new list.
# time: O(n * logn)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x.start, x.end))
        ret_list = [intervals[0]]
        for i in range(1, len(intervals)):
            if ret_list[-1].end >= intervals[i].start and intervals[i].end > ret_list[-1].end:
                # merge them
                ret_list[-1].end = intervals[i].end
            elif intervals[i].end > ret_list[-1].end:
                ret_list.append(intervals[i])
        return ret_list