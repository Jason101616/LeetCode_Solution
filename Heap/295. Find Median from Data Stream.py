# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# Examples: 
# [2,3,4] , the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2

# idea: use two heap to maintain large part of the list and small part of the list.
# use the top item of the queue and calculate the average of them.

import Queue


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_q = Queue.PriorityQueue()
        self.min_q = Queue.PriorityQueue()

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # put it in the min_q
        self.min_q.put(num)
        # pop the min value from min_q and put it in the max_q
        self.max_q.put(-self.min_q.get())
        # if len(min_q) < len(max_q), put the max value in max_q to min_q
        if self.min_q.qsize() < self.max_q.qsize():
            self.min_q.put(-self.max_q.get())

    def findMedian(self):
        """
        :rtype: float
        """
        if self.min_q.qsize() > self.max_q.qsize():
            return self.min_q.queue[0]
        else:
            return (-self.max_q.queue[0] + self.min_q.queue[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
