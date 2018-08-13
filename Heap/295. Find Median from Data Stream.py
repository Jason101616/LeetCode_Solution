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
# time: O(logn), space: O(1)
from Queue import PriorityQueue


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = PriorityQueue()
        self.minHeap = PriorityQueue()

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.minHeap.qsize() == self.maxHeap.qsize():
            self.maxHeap.put(-num)
            self.minHeap.put(-self.maxHeap.get())
        else:
            self.minHeap.put(num)
            self.maxHeap.put(-self.minHeap.get())

    def findMedian(self):
        """
        :rtype: float
        """
        if self.minHeap.qsize() == self.maxHeap.qsize():
            return (self.minHeap.queue[0] - self.maxHeap.queue[0]) / 2.0
        else:
            return self.minHeap.queue[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
