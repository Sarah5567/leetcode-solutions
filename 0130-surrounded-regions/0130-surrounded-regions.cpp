class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int n = board.size();
        if (n == 0) return;
        int m = board[0].size();

        function<void(int, int)> dfs = [&](int i, int j) {
            if (i < 0 || i >= n || j < 0 || j >= m || board[i][j] != 'O')
                return;
            board[i][j] = '#'; // תו זמני
            dfs(i+1, j);
            dfs(i-1, j);
            dfs(i, j+1);
            dfs(i, j-1);
        };

        for (int i = 0; i < n; i++) {
            dfs(i, 0);
            dfs(i, m-1);
        }
        for (int j = 0; j < m; j++) {
            dfs(0, j);
            dfs(n-1, j);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == '#') board[i][j] = 'O';
            }
        }
    }
};
