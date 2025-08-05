class Solution {
    int backtrack(int r, int n, vector<string>& board,
                   vector<bool>& col,
                   vector<bool>& diag1,
                   vector<bool>& diag2) {
        if (r == n) {
            return 1;
        }
        int count = 0;
        for (int c = 0; c < n; ++c) {
            if (col[c] || diag1[r - c + n - 1] || diag2[r + c])
                continue;

            board[r][c] = 'Q';
            col[c] = diag1[r - c + n - 1] = diag2[r + c] = true;

            count += backtrack(r + 1, n, board, col, diag1, diag2);

            board[r][c] = '.';
            col[c] = diag1[r - c + n - 1] = diag2[r + c] = false;
        }
        return count;
    }

public:
    int totalNQueens(int n){
        vector<string> board(n, string(n, '.'));
        vector<bool> col(n, false);
        vector<bool> diag1(2 * n - 1, false);
        vector<bool> diag2(2 * n - 1, false);

        return backtrack(0, n, board, col, diag1, diag2);
    }
};
