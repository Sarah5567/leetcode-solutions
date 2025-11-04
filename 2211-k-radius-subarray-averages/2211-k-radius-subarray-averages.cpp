class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int n = nums.size();
        int subarrayLength = k * 2 + 1;
        vector<int> res(n, -1);
        if(n < subarrayLength) return res;

        long long curSum = accumulate(nums.begin(), nums.begin() + (subarrayLength - 1), 0LL);

        for(int i = k; i < n - k; i++) {
            if(i > k)
                curSum -= nums[i - k - 1];
            curSum += nums[i + k];
            res[i] = curSum / subarrayLength;
        }


        return res;
    }
};