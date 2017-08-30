/*
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || k == 0)
            return head;
        int length = 1;
        ListNode *temp = head;
        while (temp->next != nullptr) {
            length++;
            temp = temp->next;
        }
        temp->next = head;
        int num = length - k % length;
        for (int i = 0; i < num; i++)
            temp = temp->next;
        head = temp->next;
        temp->next = nullptr;
        return head;
    }
};