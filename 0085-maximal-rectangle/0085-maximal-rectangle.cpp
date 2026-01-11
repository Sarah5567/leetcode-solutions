class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int rows = matrix.size();
        if (rows == 0) return 0;
        int cols = matrix[0].size();

        // Count consecutive ones from the left
        vector<vector<int>> onesFromLeft(rows, vector<int>(cols, 0));
        for (int i = 0; i < rows; i++) {
            int run = 0;
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == '1') {
                    run++;
                    onesFromLeft[i][j] = run;
                } else {
                    run = 0;
                }
            }
        }

        vector<vector<int>> highBoundery(rows, vector<int>(cols, 0));
        vector<vector<int>> lowBoundery(rows, vector<int>(cols, 0));
        stack<int> st;

        // Upper boundary
        for (int col = 0; col < cols; col++) {
            while (!st.empty()) st.pop();

            for (int row = 0; row < rows; row++) {
                int cur = onesFromLeft[row][col];
                if (cur == 0) {
                    st.push(row);
                    continue;
                }

                while (!st.empty() && onesFromLeft[st.top()][col] >= cur)
                    st.pop();

                highBoundery[row][col] = st.empty() ? 0 : st.top() + 1;
                st.push(row);
            }
        }

        // Lower boundary
        for (int col = 0; col < cols; col++) {
            while (!st.empty()) st.pop();

            for (int row = rows - 1; row >= 0; row--) {
                int cur = onesFromLeft[row][col];
                if (cur == 0) {
                    st.push(row);
                    continue;
                }

                while (!st.empty() && onesFromLeft[st.top()][col] > cur)
                    st.pop();

                lowBoundery[row][col] = st.empty() ? rows : st.top();
                st.push(row);
            }
        }

        // Compute maximal rectangle
        int maxRectangle = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int width = onesFromLeft[i][j];
                if (width == 0) continue;

                int height = lowBoundery[i][j] - highBoundery[i][j];
                maxRectangle = max(maxRectangle, width * height);
            }
        }

        return maxRectangle;
    }
};
