class Solution {
private:
    long long getPrefixSum(vector<vector<int>>& grid, vector<vector<long long>>& pref, vector<int> from, vector<int> to){
        return pref[to[0]][to[1]] - pref[from[0]][from[1]] + grid[from[0]][from[1]];
    }
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();

        vector<vector<long long>> rowPref(m, vector<long long>(n, 0));
        for(int i = 0; i < m; i++){
            rowPref[i][0] = grid[i][0];
            for(int j = 1; j < n; j++)
                rowPref[i][j] = grid[i][j] + rowPref[i][j - 1];
        }

        vector<vector<long long>> colPref(m, vector<long long>(n, 0));
        for(int j = 0; j < n; j++){
            colPref[0][j] = grid[0][j];
            for(int i = 1; i < m; i++)
                colPref[i][j] = grid[i][j] + colPref[i - 1][j];
        }

        vector<vector<long long>> upRightPref(m, vector<long long>(n, 0));
        for(int r = 0; r < m; r++){
            upRightPref[r][0] = grid[r][0];
            for(int i = r - 1, j = 1; i >= 0 && j < n; i--, j++)
                upRightPref[i][j] = grid[i][j] + upRightPref[i + 1][j - 1];
        }
        for(int c = 1; c < n; c++){
            upRightPref[m - 1][c] = grid[m - 1][c];
            for(int i = m - 2, j = c + 1; i >= 0 && j < n; i--, j++)
                upRightPref[i][j] = grid[i][j] + upRightPref[i + 1][j - 1];
        }

        vector<vector<long long>> downLeftPref(m, vector<long long>(n, 0));
        for(int r = 0; r < m; r++){
            downLeftPref[r][0] = grid[r][0];
            for(int i = r + 1, j = 1; i < m && j < n; i++, j++)
                downLeftPref[i][j] = grid[i][j] + downLeftPref[i - 1][j - 1];
        }
        for(int c = 1; c < n; c++){
            downLeftPref[0][c] = grid[0][c];
            for(int i = 1, j = c + 1; i < m && j < n; i++, j++)
                downLeftPref[i][j] = grid[i][j] + downLeftPref[i - 1][j - 1];
        }

        int longest = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                for(int k = 1; i + k < m && j + k < n; k++){
                    long long sum = getPrefixSum(grid, rowPref, {i, j}, {i, j + k});
                    bool isMagicSquare = true;

                    for(int r = i; r <= i + k && isMagicSquare; r++)
                        if(sum != getPrefixSum(grid, rowPref, {r, j}, {r, j + k}))
                            isMagicSquare = false;

                    for(int c = j; c < j + k && isMagicSquare; c++)
                        if(sum != getPrefixSum(grid, colPref, {i, c}, {i + k, c}))
                            isMagicSquare = false;

                    if(!isMagicSquare ||
                        sum != getPrefixSum(grid, upRightPref, {i + k, j}, {i, j + k}) ||
                        sum != getPrefixSum(grid, downLeftPref, {i, j}, {i + k, j + k}))
                        continue;
                    
                    longest = max(longest, k);
                }
            }
        }

        return longest + 1;
    }
};