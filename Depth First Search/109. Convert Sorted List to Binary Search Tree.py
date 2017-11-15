# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

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


# idea: first traverse the linked list, store all the value in a list. Than create tree node recursively.
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next
        root = self.create_tree(node_list)
        return root

    def create_tree(self, node_list):
        if not node_list:
            return None
        pos = len(node_list) // 2
        new_node = TreeNode(node_list[pos])
        new_node.left = self.create_tree(node_list[:pos])
        new_node.right = self.create_tree(node_list[pos + 1:])
        return new_node
