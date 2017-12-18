# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# idea: refer to http://bookshadow.com/weblog/2015/07/10/leetcode-linked-list-cycle-ii/
# 1). 使用快慢指针法，若链表中有环，可以得到两指针的交点M

# 2). 记链表的头节点为H，环的起点为E

# 2.1) L1为H到E的距离
# 2.2) L2为从E出发，首次到达M时的路程
# 2.3) C为环的周长
# 2.4) n为快慢指针首次相遇时，快指针在环中绕行的次数

# 根据L1,L2和C的定义，我们可以得到：

# 慢指针行进的距离为L1 + L2

# 快指针行进的距离为L1 + L2 + n * C

# 由于快慢指针行进的距离有2倍关系，因此：

# 2 * (L1+L2) = L1 + L2 + n * C => L1 + L2 = n * C => L1 = (n - 1)* C + (C - L2)

# 可以推出H到E的距离 = 从M出发绕环到达E时的路程

# 因此，当快慢指针在环中相遇时，我们再令一个慢指针从头节点出发


# 接下来当两个慢指针相遇时，即为E所在的位置
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow