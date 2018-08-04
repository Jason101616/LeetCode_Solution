# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

# Time:  O(n*n)
# Space: O(n)
# idea: simulate the booking of meeting rooms. A very natural and naive solution.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Room(object):
    def __init__(self, start, end, occupied):
        self.start = start
        self.end = end
        self.occupied = occupied

    def is_occupied(self, time):
        if time >= self.end:
            self.occupied = False
        return self.occupied


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.start)
        Rooms = []
        for interval in intervals:
            find_room = False
            for room in Rooms:
                if not room.is_occupied(interval.start):
                    room.start, room.end, room.occupied = interval.start, interval.end, True
                    find_room = True
                    break
            if not find_room:
                new_room = Room(interval.start, interval.end, True)
                Rooms.append(new_room)
        return len(Rooms)


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
