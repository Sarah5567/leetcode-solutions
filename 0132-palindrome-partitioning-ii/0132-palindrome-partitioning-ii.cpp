class Solution {
public:
    int minCut(string s) {
        int n = s.length();
        std::vector<std::vector<bool>> ranges(n, std::vector<bool>(n, false));
        
        for (int i = 0; i < n; i++)
            ranges[i][i] = true;
        
        for (int i = 1; i < n; i++)
            ranges[i - 1][i] = (s[i] == s[i - 1]);
        
        for (int i = 2; i < n; i++)
            for (int r = 0, c = i; c < n; r++, c++)
                ranges[r][c] = (s[r] == s[c] && ranges[r + 1][c - 1]);
        
        std::vector<int> minPartitions(n, 0);
        minPartitions[0] = 0;
        int minVal = INT_MAX;
        
        for (int i = 1; i < n; i++) {
            if (ranges[0][i]) {
                minPartitions[i] = 0;
            } else {
                for (int j = 1; j <= i; j++) {
                    if (ranges[j][i])
                        minVal = std::min(minVal, minPartitions[j - 1]);
                }
                minPartitions[i] = minVal + 1;
                minVal = INT_MAX;
            }
        }
        return minPartitions[n - 1];

    }
};