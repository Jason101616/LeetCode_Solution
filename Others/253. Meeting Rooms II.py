# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1

# Time:  O(n*log(n))
# Space: O(n)
# detect how many intervals interleave at most
from collections import defaultdict


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        cuttingPoint = set()
        startPoint = defaultdict(lambda: 0)
        endPoint = defaultdict(lambda: 0)
        for interval in intervals:
            cuttingPoint.add(interval.start)
            cuttingPoint.add(interval.end)
            startPoint[interval.start] += 1
            endPoint[interval.end] += 1

        cuttingPoint = sorted(list(cuttingPoint))
        res, curRes = 0, 0
        for point in cuttingPoint:
            curRes -= endPoint[point]
            curRes += startPoint[point]
            res = max(res, curRes)
        return res


# Time:  O(n*log(n))
# Space: O(n)
# idea: a start time means I need a room at that time.
# a end time means a room is avaliable since that time.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()
        start_index, end_index = 0, 0
        num_rooms = 0
        while start_index < len(starts):
            if starts[start_index] < ends[end_index]:
                # there is no available room now, create one and see next appointment
                num_rooms += 1
                start_index += 1
            else:
                # there is an available room now, use this one and see next appointment
                end_index += 1
                start_index += 1
        return num_rooms
