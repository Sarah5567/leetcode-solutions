class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        //initilize dp table
        vector<vector<int>> dp(obstacleGrid.size(), vector<int>(obstacleGrid[0].size(), 0));
        dp[0][0] = !obstacleGrid[0][0];

        for (int i = 0; i < obstacleGrid.size(); i++){
            for (int j = 0; j < obstacleGrid[0].size(); j++){
                if(!obstacleGrid[i][j]){
                    if(i > 0)
                        dp[i][j] += dp[i - 1][j];
                    if(j > 0)
                        dp[i][j] += dp[i][j - 1];

                }
            }
        }

        return dp[obstacleGrid.size() - 1][obstacleGrid[0].size() - 1];
    }
};