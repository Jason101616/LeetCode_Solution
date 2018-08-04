# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# idea: Sort the intervals by start and end time. Then traverse from the left of the sorted list to the right.
# Check whether current interval's end time is later than the start time of the next interval. If it is the case, then return False. In the end return True
# Time: O(nlogn)
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: (x.start, x.end))
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True
