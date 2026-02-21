class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        std::queue<TreeNode*> q;
        q.push(root);

        int cur_level = 0;
        int max_sum = INT_MIN;
        int ans = 0;

        while (!q.empty()) {
            int level_size = q.size();
            int cur_sum = 0;
            cur_level++;

            for (int i = 0; i < level_size; ++i) {
                TreeNode* node = q.front();
                q.pop();

                cur_sum += node->val;

                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }

            if (cur_sum > max_sum) {
                max_sum = cur_sum;
                ans = cur_level;
            }
        }

        return ans;
    }
};