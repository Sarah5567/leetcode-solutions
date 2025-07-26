class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        vector<vector<int>> onesFromLeft(rows, vector<int>(cols, 0));
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if(matrix[i][j] == '1'){
                    onesFromLeft[i][j] = 1;
                    if(j > 0)
                        onesFromLeft[i][j] += onesFromLeft[i][j - 1];
                }
            } 
        }

        stack<int> st;
        vector<vector<int>> highBoundery(rows, vector<int>(cols, 0));
        for(int i = 0; i < cols; i++){
            for(int j = 0; j < rows; j++){
                if(matrix[j][i] == '0')
                    st.push(j);
                else{
                    while(!st.empty() && onesFromLeft[st.top()][i] >= onesFromLeft[j][i])
                        st.pop();
                    highBoundery[j][i] = st.empty() ? 0 : st.top() + 1;
                    st.push(j);
                }
            }
            st = stack<int>();
        }

        st = stack<int>();
        vector<vector<int>> lowBoundery(rows, vector<int>(cols, 0));
        for(int i = 0; i < cols; i++){
            for(int j = rows - 1; j >= 0; j--){
                if(matrix[j][i] == '0')
                    st.push(j);
                else{
                    while(!st.empty() && onesFromLeft[st.top()][i] > onesFromLeft[j][i])
                        st.pop();
                    lowBoundery[j][i] = st.empty() ? rows : st.top();
                    st.push(j);
                }
            }
            st = stack<int>();
        }

        int maxRectangle = 0;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++)
                maxRectangle = max(maxRectangle, onesFromLeft[i][j] * (lowBoundery[i][j] - highBoundery[i][j]));
        }

        return maxRectangle;
    }
};