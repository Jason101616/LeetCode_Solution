/*
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
//Solution 1: Pass OJ, but not in-place. Actually, wrong answer.
class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return;
        int length = 0; ListNode *temp0 = head;
        while (temp0 != nullptr) {
            temp0 = temp0->next;
            length++;
        }
        ListNode **temp1 = new ListNode *[length];
        temp0 = head;
        for (int i = 0; i < length; i++) {
            temp1[i] = temp0;
            temp0 = temp0->next;
        }
        if (length % 2 == 0) {
            int i = 0;
            for (; i < length/2 - 1; i++) {
                temp1[i]->next = temp1[length - i - 1];
                temp1[length - i - 1]->next = temp1[i + 1];
            }
            temp1[i]->next = temp1[length - i - 1];
            temp1[length - i - 1]->next = nullptr;
        }
        else {
            int i = 0;
            for (; i < length/2; i++) {
                temp1[i]->next = temp1[length - i - 1];
                temp1[length - i - 1]->next = temp1[i + 1];
            }
            temp1[i]->next = nullptr;
        }
    }
};

// Solution 2: reverse second part and link first and second part.
class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return;
        //calculate length
        int length = 0; ListNode *first = head, *second;
        while (first != nullptr) {
            first = first->next;
            length++;
        }
        //make partition
        first = head;
        for (int i = 0; i < length / 2 - 1; i++)
            first = first->next;
        if (length % 2 == 0) {
            second = first->next;
            first->next = nullptr; first = head;
        } 
        else {
            second = first->next->next;
            first->next->next = nullptr; first = head;
        }
            
        //reverse second part
        ListNode *prev = nullptr; ListNode *curr = second, *nxt = second->next;
        while (curr != nullptr) {
            curr->next = prev;
            prev = curr;
            curr = nxt;
            if (nxt != nullptr)
                nxt = nxt->next;
        }
        second = prev;
        //link first and second part
        ListNode *first_nxt, *second_nxt;
        for (int i = 0; i < length / 2; i++) {
            first_nxt = first->next; second_nxt = second->next;
            first->next = second;
            second->next = first_nxt;
            first = first_nxt;
            second = second_nxt;
        }
        if (first_nxt != nullptr)
            first_nxt->next = nullptr;
    }
};