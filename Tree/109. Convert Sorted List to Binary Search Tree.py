# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted linked list: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        cnt, self.node = 0, head
        while head:
            cnt += 1
            head = head.next
        return self.helper(0, cnt - 1)

    def helper(self, l, r):
        if l > r:
            return None
        mid = l + (r - l) // 2

        left = self.helper(l, mid - 1)
        newTreeNode = TreeNode(self.node.val)
        newTreeNode.left = left

        self.node = self.node.next

        newTreeNode.right = self.helper(mid + 1, r)
        return newTreeNode
