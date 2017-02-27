/*
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
*/


class Solution {
public:
	ListNode *reverseBetween(ListNode *head, int m, int n) {
	    if(m == n) return head;
		ListNode prehead(0);
		prehead.next = head;
		ListNode *pre = &prehead;
		while (--m)
		    pre = pre->next;
		ListNode *pstart = pre->next;
		n -= m;
		while (n--) {
		    ListNode *p = pstart->next;
		    pstart->next = p->next;
		    p->next = pre->next;
		    pre->next = p;
		}
		return prehead.next;
	}
};