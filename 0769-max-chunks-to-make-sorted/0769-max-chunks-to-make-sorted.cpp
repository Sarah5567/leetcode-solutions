class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int chunks = 0;
        int border = -1;

        for(int i = 0; i < arr.size(); i++){
            border = max(border, arr[i]);
            if(i == border) chunks++;
        }
        return chunks;
    }
};