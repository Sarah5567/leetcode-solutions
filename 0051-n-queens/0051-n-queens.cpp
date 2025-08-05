class Solution {
    void backtrack(int r, int n, vector<string>& board,
                   vector<bool>& col,
                   vector<bool>& diag1,
                   vector<bool>& diag2,
                   vector<vector<string>>& res) {
        if (r == n) {
            res.push_back(board);
            return;
        }

        for (int c = 0; c < n; ++c) {
            if (col[c] || diag1[r - c + n - 1] || diag2[r + c])
                continue;

            board[r][c] = 'Q';
            col[c] = diag1[r - c + n - 1] = diag2[r + c] = true;

            backtrack(r + 1, n, board, col, diag1, diag2, res);

            board[r][c] = '.';
            col[c] = diag1[r - c + n - 1] = diag2[r + c] = false;
        }
    }

public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> board(n, string(n, '.'));
        vector<bool> col(n, false);
        vector<bool> diag1(2 * n - 1, false);
        vector<bool> diag2(2 * n - 1, false);

        backtrack(0, n, board, col, diag1, diag2, res);
        return res;
    }
};
