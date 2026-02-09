class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        const int MOD = 1e9 + 7;
        int odds = 0, evens = 0;
        int ans = 0;
        for(auto& num : arr){
            if(num % 2){
                swap(odds, evens);
                odds++;
            }
            else{
                evens++;
            }
            ans = (ans + odds) % MOD;
        }
        return ans;
    }
};