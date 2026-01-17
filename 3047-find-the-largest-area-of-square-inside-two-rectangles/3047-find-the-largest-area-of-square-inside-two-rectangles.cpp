class Solution {
public:
    bool overlap(vector<int>& bottomLeft1, vector<int>& topRight1, vector<int>& bottomLeft2, vector<int>& topRight2){
        if(min(topRight1[0], topRight2[0]) <= max(bottomLeft1[0], bottomLeft2[0]))
            return false;

        return min(topRight1[1], topRight2[1]) > max(bottomLeft1[1], bottomLeft2[1]);
    }
    long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
        int longestSide = 0, n = bottomLeft.size();

        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                if(overlap(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j])){
                    int height = min(topRight[i][1], topRight[j][1]) - max(bottomLeft[i][1], bottomLeft[j][1]);
                    int width = min(topRight[i][0], topRight[j][0]) - max(bottomLeft[i][0], bottomLeft[j][0]);
                    longestSide = max(longestSide, min(height, width));
                }
            }
        }

        return 1LL * longestSide * longestSide;
    }
};