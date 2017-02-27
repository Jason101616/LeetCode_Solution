/*
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
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
        if (head == nullptr || head->next == nullptr)
            return head;
        for (ListNode *first = head, *second = head->next; 
            second != nullptr; second = second->next) {
                if (first->val != second->val) {
                    first->next = second;
                    first = second;
                }
                if (second->next == nullptr)
                    first->next = nullptr;
        }
        return head;
    }
};