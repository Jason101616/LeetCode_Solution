/*
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
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
    bool findTarget(TreeNode* root, int k) {
        unordered_map<int, int> node;
        preorder(root, &node);
        int target;
        for (unordered_map<int, int>::iterator i = node.begin(); i != node.end(); i++) {
            target = k-i->first;
            if (node.find(target) != node.end() && node[i->first] != node[target]) {
                return true;
            }
        }
        return false;
    }
    
    void preorder(TreeNode* root, unordered_map<int, int>* node) {
        int index = 0;
        preorder_cnt(root, node, &index);
    }
    
    void preorder_cnt(TreeNode* root, unordered_map<int, int>* node, int* index) {
        if (root) {
            (*node)[root->val] = *index;
            (*index)++;
            preorder_cnt(root->left, node, index);
            preorder_cnt(root->right, node, index);
        }
    }
};