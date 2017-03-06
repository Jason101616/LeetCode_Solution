/*
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
*/
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (head == nullptr)
            return head;
        RandomListNode *new_head, *p1, *p2;
        //Build the 2nd list by creating a new node for each node in 1st list. 
        //While doing so, insert each new node after it's corresponding node in the 1st list.
        for (p1 = head; p1 != nullptr; p1 = p1->next->next) {
            p2 = new RandomListNode(p1->label);
            p2->next = p1->next;
            p1->next = p2;
        }
        //The new head is the 2nd node as that was the first inserted node.
        new_head = head->next;
        //Fix the random pointers in the 2nd list
        for (p1 = head; p1 != nullptr; p1 = p1->next->next)
            if (p1->random != nullptr)
                p1->next->random = p1->random->next;
        //Separate the combined list into 2: Splice out nodes that are part of second list.
        for (p1 = head; p1 !=nullptr; p1 = p1->next) {
            p2 = p1->next->next;
            if (p2 != nullptr)
                p1->next->next = p2->next;
            p1->next = p2;
        }
        return new_head;
    }
};