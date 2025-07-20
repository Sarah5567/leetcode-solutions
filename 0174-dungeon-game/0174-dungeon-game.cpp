using namespace std;
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size(), n = dungeon[0].size();
        vector<vector<int>> minPoint(m, vector<int>(n));

        minPoint[m - 1][n - 1] = max(-dungeon[m - 1][n - 1], 0);
        for(int i = m - 2; i >= 0; i--)
            minPoint[i][n - 1] = max(0, minPoint[i + 1][n - 1] - dungeon[i][n - 1]);
        for(int i = n - 2; i >= 0; i--){
            minPoint[m - 1][i] = max(0, minPoint[m - 1][i + 1] - dungeon[m - 1][i]);
        }

        for(int i = m - 2; i >= 0; i--){
            for(int j = n - 2; j >= 0; j--){
                minPoint[i][j] = max(0, min(minPoint[i + 1][j], minPoint[i][j + 1]) - dungeon[i][j]);
            }
        }

        return minPoint[0][0] + 1;       
    }
};