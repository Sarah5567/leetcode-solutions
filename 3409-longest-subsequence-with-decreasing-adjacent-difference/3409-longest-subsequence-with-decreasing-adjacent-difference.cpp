class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int n = nums.size();
        int max_difference = *max_element(nums.begin(), nums.end()) + 1;
        vector<vector<int>> dp(max_difference + 1, vector<int>(n + 1, 0));
        unordered_map<int, int> indexes;

        for(int difference = max_difference - 1; difference >= 0; difference--){
            for(int i = 1; i <= n; i++){
                auto idx = indexes.find(nums[i - 1] + difference);
                if(idx != indexes.end())
                    dp[difference][i] = dp[difference][idx->second] + 1;
                
                idx = indexes.find(nums[i - 1] - difference);
                if(idx != indexes.end())
                    dp[difference][i] = max(dp[difference][i], dp[difference][idx->second] + 1);

                dp[difference][i] = max(dp[difference][i], dp[difference + 1][i] );
                indexes[nums[i - 1]] = i;             
            }
            indexes.clear();
        }
        return *max_element(dp[0].begin(), dp[0].end()) + 1;
    }
};