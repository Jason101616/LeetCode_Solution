# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach 1: merge sort.
# time: O(nlogn), space: O(logn)
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # cut the linked-list into 2 halfs. length of second half >= length of first half
        prev_slow, slow, fast = None, head, head
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        prev_slow.next = None
        # sort both half
        first = self.sortList(head)
        second = self.sortList(slow)
        # merge
        return self.merge(first, second)
    
    def merge(self, first, second):
        dummy = head = ListNode(None)
        while first and second:
            if first.val < second.val:
                head.next = first
                first = first.next
            else:
                head.next = second
                second = second.next
            head = head.next
        head.next = first if first else second
        return dummy.next
            

# Approach 2: merge sort, bottom-up divide and conquer, real O(1) space, but trick. C++ version.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

/**
 * Merge sort use bottom-up policy,
 * so Space Complexity is O(1)
 * Time Complexity is O(NlgN)
 * stable sort
 */
class Solution {
  public:
    ListNode* sortList(ListNode* head) {
        if (!head || !(head->next))
            return head;

        // get the linked list's length
        ListNode* cur = head;
        int length = 0;
        while (cur) {
            length++;
            cur = cur->next;
        }

        ListNode dummy(0);
        dummy.next = head;
        ListNode *left, *right, *tail;
        for (int step = 1; step < length; step <<= 1) {
            cur = dummy.next;
            tail = &dummy;
            while (cur) {
                left = cur;
                right = split(left, step);
                cur = split(right, step);
                tail = merge(left, right, tail);
            }
        }
        return dummy.next;
    }

  private:
    /**
     * Divide the linked list into two lists,
     * while the first list contains first n ndoes
     * return the second list's head
     */
    ListNode* split(ListNode* head, int n) {
        // if(!head) return NULL;
        for (int i = 1; head && i < n; i++)
            head = head->next;

        if (!head)
            return NULL;
        ListNode* second = head->next;
        head->next = NULL;
        return second;
    }
    /**
     * merge the two sorted linked list l1 and l2,
     * then append the merged sorted linked list to the node head
     * return the tail of the merged sorted linked list
     */
    ListNode* merge(ListNode* l1, ListNode* l2, ListNode* head) {
        ListNode* cur = head;
        while (l1 && l2) {
            if (l1->val > l2->val) {
                cur->next = l2;
                cur = l2;
                l2 = l2->next;
            } else {
                cur->next = l1;
                cur = l1;
                l1 = l1->next;
            }
        }
        cur->next = (l1 ? l1 : l2);
        while (cur->next)
            cur = cur->next;
        return cur;
    }
};