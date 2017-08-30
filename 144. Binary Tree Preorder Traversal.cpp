/*
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
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
//use stack
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode *> TreeStack;
        if (root != nullptr) TreeStack.push(root);
        while (!TreeStack.empty()) {
            TreeNode *current = TreeStack.top();
            TreeStack.pop();
            ret.push_back(current->val);
            if (current->right != nullptr) TreeStack.push(current->right);
            if (current->left != nullptr) TreeStack.push(current->left);
        }
        return ret;
    }
};

//recursion
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        preTraversal(root, ret);
        return ret;
    }
    void preTraversal(TreeNode *p, vector<int> &ret) {
        if (p) {
            ret.push_back(p->val);
            preTraversal(p->left, ret);
            preTraversal(p->right, ret);
        }
    }
};