class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int prefSum = 0;
        int minPref = 0;
        int ans = INT_MIN;

        for (int num : nums) {
            prefSum += num;
            ans = max(ans, prefSum - minPref);
            minPref = min(minPref, prefSum);
        }
        return ans;
    }
};
