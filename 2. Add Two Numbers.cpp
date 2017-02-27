/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
*/


//Definition for singly - linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		ListNode temp(0);
		ListNode *cur = &temp;
		int carry = 0;
		for (ListNode *l1_temp = l1, *l2_temp = l2;
			l1_temp != nullptr || l2_temp != nullptr;
			l1_temp = (l1_temp == nullptr ? nullptr : l1_temp->next), l2_temp = (l2_temp == nullptr ? nullptr : l2_temp->next), cur = cur->next) {
			int a = (l1_temp == nullptr ? 0 : l1_temp->val);
			int b = (l2_temp == nullptr ? 0 : l2_temp->val);
			int current = (a + b + carry) % 10;
			carry = (a + b + carry) / 10;
			cur->next = new ListNode(current);
		}
		if (carry != 0)
			cur->next = new ListNode(carry);
		return temp.next;
	}
};