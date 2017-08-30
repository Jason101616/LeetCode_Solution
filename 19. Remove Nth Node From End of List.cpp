/*
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (n == 0 || head == nullptr)
            return head;
        ListNode prev(0); prev.next = head;
        ListNode *temp = head;
        int length = 1;
        while (temp->next != nullptr) {
            length++;
            temp = temp->next;
        }
        length = length - n;
        ListNode *first = &prev;
        for (int i = 0; i < length; i++)
            first = first->next;
        first->next = first->next->next;
        return prev.next;
    }
};