class Solution {
private:
    const long long MOD = 1000000007;
    long long modPow(long long base, long long exponent) {
        long long res = 1;
        base %= MOD;
        while (exponent > 0) {
            if (exponent & 1)
                res = (__int128)res * base % MOD;
            base = (__int128)base * base % MOD;
            exponent >>= 1;
        }
        return res;
    }
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        if(multiplier == 1)
            return nums;

        priority_queue<
            pair<long long ,int>,
            vector<pair<long long,int>>,
            greater<pair<long long,int>>
        > pq;

        int maxValue = INT_MIN;
        for (int i = 0; i < nums.size(); i++){
            pq.push({nums[i], i});
            maxValue = max(maxValue, nums[i]);
        }

        int i;
        for(i = 1; i <= k; i++){
            auto [val, idx] = pq.top();
            pq.pop();
            pq.push({val * multiplier, idx});
            if(val * multiplier > maxValue)
                break;
        }
        int remaining = max(0, k - i);
        vector<int> res(nums.size());

        for(int pos = 1; !pq.empty(); pos++){
            auto [val, idx] = pq.top();
            pq.pop();
            int exponent = remaining / nums.size() + (pos <= remaining % nums.size());
            res[idx] = (__int128)val * modPow(multiplier, exponent) % MOD;
        }

        return res;
    }
};