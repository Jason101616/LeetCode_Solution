# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

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
# 插入newInterval的算法为：扫描队列中每个interval I[i]：
# 如果newInterval已经被插入了，则只要插入I(i)就行。
# 如果newInterval在I(i)前，则先插入newInterval再插入I(i)。
# 如果newInterval和I(i)有重合，则将I(i)合并入newInterval，但并不插入结果。
# 如果newInterval在I(i)后，则插入I(i)到结果。

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        res = []
        isInserted = False
        for interval in intervals:
            if isInserted:
                res.append(interval)
            elif interval.end < newInterval.start:
                res.append(interval)
            elif interval.start > newInterval.end:
                res.append(newInterval)
                res.append(interval)
                isInserted = True
            elif self.isOverlap(newInterval, interval):
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)
        if not isInserted:
            res.append(newInterval)
        return res

    def isOverlap(self, i1, i2):
        return not (i1.end < i2.start or i2.end < i1.start)
