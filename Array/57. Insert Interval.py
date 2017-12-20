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