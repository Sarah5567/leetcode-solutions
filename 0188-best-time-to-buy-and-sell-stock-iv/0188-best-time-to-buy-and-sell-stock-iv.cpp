#include <algorithm>

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int const ROWS = k + 1, COLS = prices.size();
        int** dp = new int*[ROWS];
        for(int i = 0; i < ROWS; i++){
            dp[i] = new int[COLS]();
        }

        for(int i = 1; i < ROWS; i++){
            int max_profit = -prices[0];
            for(int j = 1; j < COLS; j++){
                max_profit = std::max(max_profit, dp[i - 1][j - 1] - prices[j]);
                dp[i][j] = std::max(dp[i][j - 1],  max_profit + prices[j]);
            }
        }

        int res = dp[ROWS - 1][COLS - 1];

        for(int i = 0; i < ROWS; i++)
            delete[] dp[i];
        delete[] dp;

        return res;
    }
};