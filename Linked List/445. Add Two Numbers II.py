# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Use a stack to add the linked list
# Time: O(n), Space: O(n)

class Solution(object):
    def addTwoNumbers(self, l1, l2, none=None):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        prevNode = none
        while stack1 or stack2:
            curSum = carry
            if stack1:
                curSum += stack1.pop()
            if stack2:
                curSum += stack2.pop()
            newNode = ListNode(curSum % 10)
            newNode.next = prevNode
            prevNode = newNode
            carry = curSum // 10
        if carry > 0:
            newNode = ListNode(1)
            newNode.next = prevNode
            prevNode = newNode
        return prevNode
