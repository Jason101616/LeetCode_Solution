/*
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
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
	ListNode *detectCycle(ListNode *head) {
		unordered_map<ListNode *, bool> visited;
		for (ListNode *p = head; p != nullptr; p = p->next) {
			unordered_map<ListNode *, bool>::const_iterator find = visited.find(p);
			if (find == visited.end())
				visited[p] = false;
			else
				return p;
		}
		return nullptr;
	}
};

