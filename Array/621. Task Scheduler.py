# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.

# Example 1:
# Input: tasks = ['A','A','A','B','B','B'], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].

from collections import defaultdict
from queue import PriorityQueue


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = defaultdict(lambda: 0)
        for task in tasks:
            counter[task] += 1

        pq = PriorityQueue()
        for cnt in counter.values():
            pq.put(-cnt) # because python pq is ascending

        res = 0
        while pq.qsize() > 0:
            tmpBuffer = []
            for i in range(n + 1):
                tmp = pq.get()
                if tmp + 1 < 0: # there are remaining tasks
                    tmpBuffer.append(tmp + 1)
                res += 1
                if pq.qsize() == 0: # cannot execute more tasks on this cycle
                    if len(tmpBuffer) > 0:
                        res += (n - i)
                    break
            for cnt in tmpBuffer:
                pq.put(cnt)
        return res
