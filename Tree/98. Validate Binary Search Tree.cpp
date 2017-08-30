/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 /*
  If a BST is valid, the val of the inorder traversal of the tree is ascending.
  */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        TreeNode* prev = nullptr;
        return isValid(root, prev);
    }
    
    bool isValid(TreeNode* cur, TreeNode* &prev) {
        if (cur == nullptr) {
            return true;
        }
        return isValid(cur->left, prev) && check(cur, prev) && isValid(cur->right, prev);
    }
    
    bool check(TreeNode* cur, TreeNode* &prev) {
        if (prev == nullptr) {
            prev = cur;
            return true;
        }
        if (cur->val <= prev->val) {
            return false;
        }
        prev = cur;
        return true;
    }
};