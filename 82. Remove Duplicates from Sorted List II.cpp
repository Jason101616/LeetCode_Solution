/*
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr)
            return head;
        ListNode prev(0); ListNode *pre = &prev; pre->next = head;
        ListNode *cur = head;
        while (cur != nullptr) {
            bool duplicated = false;
            if (cur->next != nullptr && cur->val == cur->next->val)
                duplicated = true;
            if (duplicated) {
                ListNode *temp = cur->next;
                while (temp != nullptr) {   //cur->(next not duplicated node) or break
                    if (temp-> val != cur->val) {
                        cur = temp; break;
                    }
                    else
                        temp = temp->next;
                }
                if (temp == nullptr) break;
                continue;
            }
            else {
                pre->next = cur;
                pre = pre->next;
                cur = cur->next;
            }
        }
        pre->next = nullptr;
        return prev.next;
    }
};