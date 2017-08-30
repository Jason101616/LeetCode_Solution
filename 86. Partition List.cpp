/*
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode node0(0);ListNode node1(0);
        ListNode *ptr0 = &node0;ListNode *ptr1 = &node1;
        for (ListNode *cur = head; cur != nullptr; cur = cur->next)
            if (cur->val < x)
                ptr0 = ptr0->next = cur;
            else
                ptr1 = ptr1->next = cur;
        ptr1->next = nullptr;
        ptr0->next = node1.next;
        return node0.next;
    }
};