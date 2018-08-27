# Given a binary tree

# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Note:

# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# Example:

# Given the following binary tree,

#      1
#    /  \
#   2    3
#  / \    \
# 4   5    7
# After calling your function, the tree should look like:

#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \    \
# 4-> 5 -> 7 -> NULL

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# level order traversal:
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        queue = collections.deque([root])
        while queue:
            curLevelLen = len(queue)
            for i in range(curLevelLen):
                node = queue.popleft()
                node.next = queue[0] if i != curLevelLen - 1 else None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

# Iteratively (Java):
# /**
#  * Definition for binary tree with next pointer.
#  * public class TreeLinkNode {
#  *     int val;
#  *     TreeLinkNode left, right, next;
#  *     TreeLinkNode(int x) { val = x; }
#  * }
#  */
# public class Solution {
#     //based on level order traversal
#     public void connect(TreeLinkNode root) {
#
#         TreeLinkNode head = null; //head of the next level
#         TreeLinkNode prev = null; //the leading node on the next level
#         TreeLinkNode cur = root;  //current node of current level
#
#         while (cur != null) {
#
#             while (cur != null) { //iterate on the current level
#                 //left child
#                 if (cur.left != null) {
#                     if (prev != null) {
#                         prev.next = cur.left;
#                     } else {
#                         head = cur.left;
#                     }
#                     prev = cur.left;
#                 }
#                 //right child
#                 if (cur.right != null) {
#                     if (prev != null) {
#                         prev.next = cur.right;
#                     } else {
#                         head = cur.right;
#                     }
#                     prev = cur.right;
#                 }
#                 //move to next node
#                 cur = cur.next;
#             }
#
#             //move to next level
#             cur = head;
#             head = null;
#             prev = null;
#         }
#
#     }
# }
