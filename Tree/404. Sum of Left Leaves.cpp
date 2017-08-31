/*
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int sum = 0;
        sum_left_leaves(root, &sum, nullptr);
        return sum;
    }
    void sum_left_leaves(TreeNode* cur, int* sum, TreeNode* prev) {
        if (cur == nullptr) {
            return;
        }
        if (prev == nullptr && cur->left == nullptr && cur->right == nullptr) {
            *sum = 0;
            return;
        }
        if (cur->left == nullptr && cur->right == nullptr && cur == prev->left) {
            *sum += cur->val;
        }
        else {
            sum_left_leaves(cur->left, sum, cur);
            sum_left_leaves(cur->right, sum, cur);
        }
    }
};