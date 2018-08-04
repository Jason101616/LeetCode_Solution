# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Approach 1: intuitive solution
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = self.no_need_split(intervals, newInterval)
        if res:
            return res
        start, end = None, None
        for index, interval in enumerate(intervals):
            if self.is_interleave(interval, newInterval):
                start = index
                for i in range(index + 1, len(intervals)):
                    if not self.is_interleave(intervals[i], newInterval):
                        end = i - 1
                        break
                break
        return self.merge(newInterval, intervals, start, end)

    def is_interleave(self, interval1, interval2):
        if interval1.end < interval2.start or interval1.start > interval2.end:
            return False
        return True

    def merge(self, newInterval, intervals, start, end):
        if end == None:
            end = len(intervals) - 1
        left_part = intervals[:start]
        right_part = intervals[end + 1:]
        new_interval = Interval()
        new_interval.start = min(newInterval.start, intervals[start].start, intervals[end].start)
        new_interval.end = max(newInterval.end, intervals[start].end, intervals[end].end)
        mid_part = [new_interval]
        return left_part + mid_part + right_part

    def no_need_split(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        elif newInterval.end < intervals[0].start:
            return [newInterval] + intervals
        elif newInterval.start > intervals[-1].end:
            return intervals + [newInterval]
        prev = None
        for i in range(len(intervals)):
            if self.is_interleave(newInterval, intervals[i]):
                return None
            if prev and prev.end < newInterval.start and intervals[i].start > newInterval.end:
                intervals.insert(i, newInterval)
                return intervals
            prev = intervals[i]


# Approach 2: written by other person
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# 两个interval有重合有很多种可能性，但判断它们不重合则比较简单直观。无非两种情况：
# (1) [s1, e1]  [s2, e2]：即s2>e1
# (2) [s2, e2]  [s1, e1]：即s1>e2
# 不重合的条件为：s2>e1 || s1>e2，反之则重合。

# 对于两个有重合的interval： [s1, e1]，[s2, e2]。合并后变为[min(s1,s2), max(e1,e2)]。
# 插入interval a的算法为：扫描队列中每个interval I[i]：
# 如果a已经被插入了，则只要插入I(i)就行。
# 如果a在I(i)前，则先插入a再插入I(i)到结果。
# 如果a和I(i)有重合，则将I(i)合并入a，但并不插入结果。
# 如果a在I(i)后，则插入I(i)到结果。
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ret_list = []
        is_insert = False
        for i in range(len(intervals)):
            if is_insert:
                ret_list.append(intervals[i])
                continue
            if newInterval.end < intervals[i].start:
                ret_list.append(newInterval)
                ret_list.append(intervals[i])
                is_insert = True
                continue
            if not (newInterval.start > intervals[i].end or intervals[i].start > newInterval.end):
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
                continue
            ret_list.append(intervals[i])
        if not is_insert:
            ret_list.append(newInterval)
        return ret_list
