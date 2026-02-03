class Solution {
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        static constexpr int MOD = 1'000'000'007;

        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);

        sort(idx.begin(), idx.end(),
             [&](int i, int j) { return efficiency[i] > efficiency[j]; });

        priority_queue<int, vector<int>, greater<int>> pq;
        long long sum_speeds = 0;
        long long best = 0;

        for (int i = 0; i < n; ++i) {
            const int cur = idx[i];
            const int sp = speed[cur];
            const int eff = efficiency[cur];

            if (i == 0) {
                pq.push(sp);
                sum_speeds = sp;
                best = 1LL * sp * eff;
                continue;
            }

            if (i < k || pq.top() <= sp) {
                if (i >= k) {
                    sum_speeds -= pq.top();
                    pq.pop();
                }
                sum_speeds += sp;
                pq.push(sp);

                const long long perf = sum_speeds * 1LL * eff;
                if (perf > best) best = perf;
            }
        }

        return (int)(best % MOD);
    }
};
