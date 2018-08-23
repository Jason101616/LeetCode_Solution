# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # find the middle point of the linked list
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second part
        prev = slow
        start = prev.next
        then = start.next
        while then:
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        # reorder one by one
        l1, l2 = head, slow.next
        while l1 != slow:
            slow.next = l2.next
            l1Nxt = l1.next
            l2Nxt = l2.next
            l2.next = l1.next
            l1.next = l2
            l1 = l1Nxt
            l2 = l2Nxt