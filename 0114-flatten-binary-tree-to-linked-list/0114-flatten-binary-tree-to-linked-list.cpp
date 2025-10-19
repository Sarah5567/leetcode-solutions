/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* flattenRecuresively(TreeNode* root){
        if(!root || (!root->right && !root->left))
            return root;

        TreeNode* rightChild = nullptr;
        if(root->left){
            rightChild = root->right;
            root->right = root->left;
            root->left = nullptr;
        }

        TreeNode* next = flattenRecuresively(root->right);
        if(rightChild){
            next->right = rightChild;
            return flattenRecuresively(next->right);
        }
        else
            return next;
    }
    void flatten(TreeNode* root) {
       flattenRecuresively(root);
    }
};