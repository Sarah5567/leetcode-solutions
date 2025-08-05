class Solution {
bool is_valid(vector<string> board, int r, int c){
    for(int i = 0; i < r; i++)
        if(board[i][c] == 'Q')
            return false;

    for(int i = r - 1, j = c - 1; i >= 0 && j >= 0; i--, j--)
        if(board[i][j] == 'Q')
            return false;

    for(int i = r - 1, j = c + 1; i >= 0 && j < board.size(); i--, j++)
        if(board[i][j] == 'Q')
            return false;

    return true;
}
void all_queens_options(vector<vector<string>>& res, vector<string> board, int r, int n){
    if(r == n){
        res.push_back(board);
    }
    else{
       for(int i = 0; i < n; i++)
            if(is_valid(board, r, i)){
                board[r][i] = 'Q';
                all_queens_options(res, board, r + 1, n);
                board[r][i] = '.';
            }
    }
}
public:
    vector<vector<string>> solveNQueens(int n) {
    vector<string> board(n, string(n, '.'));
    vector<vector<string>> res;
    all_queens_options(res, board, 0, n);
    return res;
    }
};