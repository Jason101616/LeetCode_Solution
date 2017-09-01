/*
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
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
    TreeNode* convertBST(TreeNode* root) {
        vector<int> in_order_val;
        in_order(root, &in_order_val);
        vector<int> plus(in_order_val.size());
        int duplicate = 1;
        for (auto i = in_order_val.rbegin(), j = plus.rbegin(); 
             i != in_order_val.rend(); i++, j++) {
            if (j == plus.rbegin()) {
                *j = 0;
            }
            else {
                if (*i == *(i - 1)) {
                    *j = *(j - 1);
                    duplicate++;
                }
                else {
                    *j = *(j - 1) + (*(i - 1)) * duplicate;
                    duplicate = 1;
                }
            }
        }
        int cnt = 0;
        in_order_add(root, &plus, &cnt);
        return root;
    }
    
    void in_order(TreeNode* root, vector<int>* in_order_val) {
        if (root) {
            in_order(root->left, in_order_val);
            (*in_order_val).push_back(root->val);
            in_order(root->right, in_order_val);
        }
    }
    
    void in_order_add(TreeNode* root, vector<int>* plus, int* cnt) {
        if (root) {
            in_order_add(root->left, plus, cnt);
            root->val += (*plus)[*cnt];
            (*cnt)++;
            in_order_add(root->right, plus, cnt);
        }
    }
};