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
    int maxPathFromNode(TreeNode* node, int& maxSum){
        if(!node)
            return 0;
        
        int leftMaxPath = maxPathFromNode(node->left, maxSum);
        int rightMaxPath = maxPathFromNode(node->right, maxSum);

        int maxPathWithCur = node->val + max({0, leftMaxPath, rightMaxPath});
        int maxSumWithCur = node->val + max(0, leftMaxPath) + max(0, rightMaxPath);

        maxSum = max(maxSum, maxSumWithCur);
        return maxPathWithCur;
    }
    int maxPathSum(TreeNode* root) {
        int maxSum = INT_MIN;
        maxPathFromNode(root, maxSum);
        return maxSum;
    }
};