# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# naive idea: use an array to store the value of each node. And compare the value one by one.
# This idea will need extra space of O(n)

# O(1) space idea:
# Firstly, reverse the first half of the linked list. The trick is to define a fast pointer with stride of two each time.
# When decide the head of the second half, we should be careful about the total number of the nodes.
# If it is odd, we should let the head of the second half be cur.next.
# Secondly, compare the value of the reverse part with the second half one by one.
# At the same time, reverse the first half again to restore the initial state.

# Time:  O(n)
# Space: O(1)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        prev, cur, nxt, fast = None, head, head.next, head
        while fast and fast.next:
            fast = fast.next.next
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = nxt.next

        if fast:
            head_2half = cur.next
        else:
            head_2half = cur

        nxt = prev.next
        tmp = cur
        cur = prev
        prev = tmp

        while cur:
            if cur.val != head_2half.val:
                return False
            head_2half = head_2half.next
            cur.next = prev
            prev = cur
            cur = nxt
            if nxt != None:
                nxt = nxt.next
        return True
