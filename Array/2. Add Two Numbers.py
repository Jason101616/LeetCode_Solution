# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# approach 1: iteratively
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = cur_node = ListNode(None)
        while l1 and l2:
            cur_val = l1.val + l2.val + carry
            carry = cur_val // 10
            cur_val %= 10
            cur_node.next = ListNode(cur_val)
            l1 = l1.next
            l2 = l2.next
            cur_node = cur_node.next
        l1 = l1 if l1 else l2
        while l1:
            cur_val = l1.val + carry
            carry = cur_val // 10
            cur_val %= 10
            cur_node.next = ListNode(cur_val)
            l1 = l1.next
            cur_node = cur_node.next
        if carry:
            cur_node.next = ListNode(carry)
        return dummy.next


# approach 2: recursively
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.add_num(l1, l2, 0)

    def add_num(self, l1, l2, carry):
        if not l1 and not l2 and carry == 0:
            return None
        res = 0
        res += carry
        if l1:
            res += l1.val
        if l2:
            res += l2.val
        new_node = ListNode(res % 10)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        new_node.next = self.add_num(l1, l2, res // 10)
        return new_node
