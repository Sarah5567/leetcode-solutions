class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int right = min(n, citations[n - 1]), left = 1;

        while(left <= right){
            int mid = left + (right - left) / 2;
            
            if(citations[n - mid] >= mid)
                left = mid + 1;      
            else
                right = mid - 1;
        }

        return right;
    }
};