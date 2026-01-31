class Solution {
public:
    int getMoneyAmount(int n) {
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));

        for(int i = 1; i <= n; i++){
            for(int r = 1, c = i + 1; c <= n; r++, c++){
                dp[r][c] = INT_MAX;
                for(int j = r; j <= c; j++){
                    int money = j + max(dp[r][j - 1], dp[j + 1][c]);
                    dp[r][c] = min(dp[r][c], money);
                }
            }
        }
        return dp[1][n];
    }
};