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

import queue


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # count the frequency of each task
        count_freq = {}
        for task in tasks:
            if task not in count_freq:
                count_freq[task] = 1
            else:
                count_freq[task] += 1

        # put the frequency of each task into a priority queue. largest frequency should be in the front of the queue.
        # use '-' here because PriorityQueue in python can only sort ascendingly. We want it decendingly.
        freq_queue = queue.PriorityQueue()
        for task in count_freq.keys():
            freq_queue.put(-count_freq[task])

        intervals = 0
        cycle = n + 1
        while not freq_queue.empty():
            tmp_freq, time = [], 0
            # the pop out cycle, we pop out the task with largest frequency.
            # need to store it in a tmp list, because we may insert it back again.
            for _ in range(cycle):
                if not freq_queue.empty():
                    tmp_freq.append(freq_queue.get())
                    time += 1
                else:
                    break
            # if the frequency - 1 != 0, we must insert it to the PriorityQueue again
            for freq in tmp_freq:
                freq += 1
                if freq:
                    freq_queue.put(freq)

            intervals += cycle if not freq_queue.empty() else time

        return intervals
