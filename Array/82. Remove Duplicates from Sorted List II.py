# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = left = prev_prev = ListNode(None)
        prev, cur = head, head.next
        while cur:
            if cur.val != prev.val:
                if prev_prev.val == None or prev.val != prev_prev.val:
                    left.next = prev
                    left = left.next
            prev_prev = prev
            prev = cur
            cur = cur.next
        if prev.val != prev_prev.val:
            left.next = prev
            left = left.next
        left.next = None
        return dummy.next