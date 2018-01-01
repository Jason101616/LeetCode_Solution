# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

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
        dummy = left = ListNode(None)
        prev, cur = head, head.next
        while cur:
            if cur.val != prev.val:
                left.next = prev
                left = left.next
            cur = cur.next
            prev = prev.next
        left.next = prev
        return dummy.next
        