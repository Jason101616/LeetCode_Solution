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
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == nullptr) {
            return false;
        }
        int value = 0;
        return has_path(root, sum, value);
    }
    bool has_path(TreeNode* cur, int sum, int value) {
        value += cur->val;
        if (cur->left == nullptr && cur->right == nullptr) {
            if (value == sum) {
                return true;
            }
            else  {
                return false;
            }
        }
        if (cur->left != nullptr && cur->right != nullptr) {
            return has_path(cur->left, sum, value) || has_path(cur->right, sum, value);
        }
        else if (cur->left != nullptr && cur->right == nullptr) {
            return has_path(cur->left, sum, value);
        }
        else if (cur->left == nullptr && cur->right != nullptr) {
            return has_path(cur->right, sum, value);
        }
    }
};