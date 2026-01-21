class Solution {
public:
    int minLength(vector<int>& nums, int k) {
        unordered_map<int,int> table;
        table.reserve(nums.size());

        int shortest = INT_MAX;
        long long sum = 0;
        int l = 0;
        const int n = (int)nums.size();

        for (int r = 0; r < n; ++r) {
            auto [it, inserted] = table.try_emplace(nums[r], 0);

            if (it->second > 0) {
                ++(it->second);
                continue;
            }

            it->second = 1;
            sum += nums[r];

            while (true) {
                int x = nums[l];
                auto itL = table.find(x); // should exist
                if (itL->second > 1) {
                    --(itL->second);
                    ++l;
                    continue;
                }
                if (sum - x >= k) {
                    --(itL->second);      // becomes 0
                    sum -= x;
                    ++l;
                    continue;
                }
                break;
            }

            if (sum >= k) {
                shortest = min(shortest, r - l + 1);
            }
        }

        return (shortest == INT_MAX) ? -1 : shortest;
    }
};
