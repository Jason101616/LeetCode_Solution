/*
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
 */

// method1: store every layer (include nullptr), Memory Limit Exceeded 
/**
 * Definition for a binary tree node. */
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1 == nullptr) {
            return t2;
        }
        if (t2 == nullptr) {
            return t1;
        }
        TreeNode* ret_merge, * tmp_t1, * tmp_t2, *tmp_merge;
        queue<TreeNode*> store_t1, store_t2, store_merge;
        store_t1.push(t1); store_t2.push(t2);
        int layer = 0;
        bool all_null;
        while (!store_t1.empty() || !store_t2.empty()) {
            all_null = true;
            int n = (int)pow(2, layer);
            if (layer == 0) {
                tmp_t1 = store_t1.front(); tmp_t2 = store_t2.front();
                tmp_merge = generate_new_node(tmp_t1, tmp_t2, &store_t1, &store_t2);
                ret_merge = tmp_merge;
                store_merge.push(tmp_merge);
                if (tmp_t1->left != nullptr || tmp_t1->right != nullptr ||
                   tmp_t2->left != nullptr || tmp_t2->right != nullptr) {
                    all_null = false;
                }
            }
            else {
                for (int i = 0; i < n; i++) {
                    /*
                     for each layer in t1 and t2, generate new node by merging the value of them,
                     and push the new node to the queue of merge.
                     then pop current layer and push the next layer in queue.
                     for each layer in merge, connect with previous layer.
                     */
                    tmp_t1 = store_t1.front(); tmp_t2 = store_t2.front();
                    tmp_merge = generate_new_node(tmp_t1, tmp_t2, &store_t1, &store_t2);
                    if (store_merge.front() != nullptr) {
                       if (i % 2 == 0) {
                            store_merge.front()->left = tmp_merge;
                        }
                        else {
                            store_merge.front()->right = tmp_merge;
                            store_merge.pop();
                        } 
                    }
                    else {
                        if (i % 2 != 0) {
                            store_merge.pop();
                        }
                    }
                    store_merge.push(tmp_merge);
                    if ((tmp_t1 != nullptr && (tmp_t1->left != nullptr || tmp_t1->right != nullptr)) ||
                       (tmp_t2 != nullptr && (tmp_t2->left != nullptr || tmp_t2->right != nullptr))) {
                        all_null = false;
                    }
                }
            }
            layer++;
            if (all_null) {
                break;
            }
        }
        return ret_merge;
    }
    
    TreeNode* generate_new_node(TreeNode* t1, TreeNode* t2, queue<TreeNode*>* store_t1, queue<TreeNode*>* store_t2) {
        TreeNode* ret = new TreeNode(0);
        if (t1 != nullptr && t2 != nullptr) {
            ret->val = t1->val + t2->val;
            (*store_t1).push(t1->left); (*store_t1).push(t1->right); (*store_t1).pop();
            (*store_t2).push(t2->left); (*store_t2).push(t2->right); (*store_t2).pop();
        }
        else if (t1 != nullptr && t2 == nullptr) {
            ret->val = t1->val;
            (*store_t1).push(t1->left); (*store_t1).push(t1->right); (*store_t1).pop();
            (*store_t2).push(nullptr); (*store_t2).push(nullptr); (*store_t2).pop();
        }
        else if (t1 == nullptr && t2 != nullptr) {
            ret->val = t2->val;
            (*store_t1).push(nullptr); (*store_t1).push(nullptr); (*store_t1).pop();
            (*store_t2).push(t2->left); (*store_t2).push(t2->right); (*store_t2).pop();
        }
        else {
            ret = nullptr;
            (*store_t1).push(nullptr); (*store_t1).push(nullptr); (*store_t1).pop();
            (*store_t2).push(nullptr); (*store_t2).push(nullptr); (*store_t2).pop();
        }
        return ret;
    }
};


// Method2: merge trees recursively
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1 && t2) {
            TreeNode* new_node = new TreeNode(t1->val + t2->val);
            new_node->left = mergeTrees(t1->left, t2->left);
            new_node->right = mergeTrees(t1->right, t2->right);
            return new_node;
        }
        else {
            return t1 ? deep_copy(t1) : deep_copy(t2); 
        }
    }
    TreeNode* deep_copy(TreeNode* t) {
        if (t == nullptr) {
            return t;
        }
        TreeNode* new_node = new TreeNode(t->val);
        new_node->left = deep_copy(t->left);
        new_node->right = deep_copy(t->right);
        return new_node;
    }
};