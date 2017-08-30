/*
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
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
	ListNode* swapPairs(ListNode* head) {
	    if (head == nullptr || head->next == nullptr)
	        return head;
        ListNode pre_head(0);
        ListNode *prev = &pre_head;
        ListNode *cur = head, *next = head->next;
        while (next != nullptr) {
            prev->next = next;
            cur->next = next->next;
            next->next = cur;
            prev = cur;
            cur = cur->next;
            next = (cur == nullptr ? nullptr : cur->next);
        }
        return pre_head.next;
	}
};