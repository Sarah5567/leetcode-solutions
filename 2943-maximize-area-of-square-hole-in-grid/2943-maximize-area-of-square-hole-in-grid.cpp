class Solution {
public:
    int maxLength(vector<int>& bars){
        sort(bars.begin(), bars.end());

        int longest = 1, curLength = 1;
        for(int i = 1; i < bars.size(); i++){
            if (bars[i] == bars[i - 1] + 1)
                curLength++;
            else
                curLength = 1;
         
            longest = max(longest, curLength);
        }
        return longest;
    }
    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {

        int length = min(maxLength(hBars), maxLength(vBars)) + 1;
        return length * length;
    }
};