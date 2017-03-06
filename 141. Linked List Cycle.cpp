/*
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
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
    bool hasCycle(ListNode *head) {
        if (head == nullptr) return head;
        ListNode *p1 = head, *p2 = head;
        while (p1 != nullptr) {
            if (p1->next == nullptr) return false;
            else p1 = p1->next->next;
            p2 = p2->next;
            if (p1 == p2) return true;
        }
        return false;
    }
};