/*
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
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