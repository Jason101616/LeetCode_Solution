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
# idea:
# Firstly, reverse the first half of the linked list. The trick is to define a fast pointer with stride of two each time.
# When decide the head of the second half, we should be careful about the number of the nodes.
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
        
        fast = head
        prev = None
        cur = head
        nxt = head.next
        while fast and fast.next:
            fast = fast.next.next
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = cur.next
        if not fast:
            head_second_half = cur
        else:
            head_second_half = cur.next
        
        nxt = prev.next
        while prev:
            if prev.val != head_second_half.val:
                return False
            prev.next = cur
            cur = prev
            prev = nxt
            if not prev:
                break
            else:
                nxt = prev.next
            head_second_half = head_second_half.next
        
        return True
            
            