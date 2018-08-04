# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach 1: use pq
# time: O(Nlogk)
# space: O(k), k is the space of pq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import Queue


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = Queue.PriorityQueue()
        dummy = tmp = ListNode(None)
        for node in lists:
            if node:
                q.put((node.val, node))
        while not q.empty():
            cur = q.get()
            tmp.next = cur[1]
            tmp = tmp.next
            if cur[1].next:
                q.put((cur[1].next.val, cur[1].next))
        return dummy.next


# Approach 2: use divide and conquer. Most optimized approach.
# time: O(Nlogk)
# space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        num_lists = len(lists)
        interval = 1
        while interval < num_lists:
            for i in range(0, num_lists - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        prev = dummy = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return dummy.next
