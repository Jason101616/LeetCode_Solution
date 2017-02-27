/*
Reverse a singly linked list.
A linked list can be reversed either iteratively or recursively. Could you implement both?
*/

//Recursive version
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
    ListNode* reverseList(ListNode* head) {
        ListNode *prev = nullptr;
        ListNode *curr = head;
        while (curr != nullptr) {
            ListNode *next_temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_temp;
        }
        return prev;
    }
};

//Iterative version
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
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr)
            return head;
        ListNode *temp = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return temp;
    }
};