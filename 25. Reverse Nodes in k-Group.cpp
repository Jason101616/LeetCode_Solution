/*
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
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
	ListNode* reverseKGroup(ListNode* head, int k) {
		if (head == nullptr || head->next == nullptr || k == 1) return head;
		ListNode *temp = head;
		int length = 0;
		while (temp != nullptr) {
			length++;
			temp = temp->next;
		}
		int n = length / k; // n times
		ListNode prev(0);
		ListNode *pre = &prev, *cur = head, *nxt = head->next;
		pre->next = head;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < k - 1; j++) {
				cur->next = nxt->next;
				nxt->next = pre->next;
				pre->next = nxt;
				nxt = cur->next;
			}
			if (cur->next != nullptr) {
				pre = cur;
				cur = nxt;
				nxt = nxt->next;
			}
			else
				break;
		}
		return prev.next;
	}
};