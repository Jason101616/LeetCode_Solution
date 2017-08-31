/*
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ret;
        if (root == nullptr) {
            return ret;
        }
        string cur_str = "";
        BTP(root, &ret, cur_str);
        return ret;
    }
    void BTP(TreeNode* cur, vector<string>* ret, string cur_str) {
        if (cur == nullptr) {
            return;
        }
        if (cur_str == "") {
            cur_str = to_string(cur->val);
        }
        else {
            cur_str += ("->" + to_string(cur->val));
        }
        if (cur->left == nullptr && cur->right == nullptr) {
            (*ret).push_back(cur_str);
        }
        else {
            BTP(cur->left, ret, cur_str);
            BTP(cur->right, ret, cur_str);
        }
    }
};