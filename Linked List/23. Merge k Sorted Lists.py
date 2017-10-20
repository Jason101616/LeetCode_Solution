# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

from Queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# time: O(Nlogk)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        node_queue = PriorityQueue()
        for head in lists:
            if head:
                node_queue.put((head.val, head))
        ret_node = tmp_node = ListNode(None)
        while not node_queue.empty():
            cur_node = node_queue.get()[1]
            ret_node.next = ListNode(cur_node.val)
            ret_node = ret_node.next
            if cur_node.next:
                node_queue.put((cur_node.next.val, cur_node.next))
        return tmp_node.next
    