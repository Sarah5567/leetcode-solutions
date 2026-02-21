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
    int maxLevelSum(TreeNode* root) {
        queue<pair<TreeNode*,int>> q;
        q.emplace(root, 1);

        int cur_sum = 0;
        int cur_level = 1;
        int max_sum = INT_MIN;
        int ans;
        while(!q.empty()){
            auto [node, level] = q.front();
            q.pop();
            if(level == cur_level + 1){
                if(cur_sum > max_sum){
                    max_sum = cur_sum;
                    ans = cur_level;
                }
                cur_level += 1;
                cur_sum = 0;
            }
            cur_sum += node->val;

            if(node->left){
                q.emplace(node->left, level + 1);
            }
            if(node->right){
                q.emplace(node->right, level + 1);
            }
        }
        if(cur_sum > max_sum)
            ans = cur_level;
        
        return ans;
    }
};