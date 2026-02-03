class Solution {
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        const int MOD = 1'000'000'007;

        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);

        sort(idx.begin(), idx.end(),
                [&](int i, int j) {
                    return efficiency[i] > efficiency[j];
                });

        

        priority_queue<int, vector<int>, greater<int>> pq;
        pq.push(speed[idx[0]]);

        long long max_performance = speed[idx[0]] * (long long)efficiency[idx[0]];
        long long sum_speeds = speed[idx[0]];

        for(int i = 1; i < n; i++){
            int cur_idx = idx[i];

            if(i < k || pq.top() <= speed[cur_idx]){
                if(i >= k){
                    sum_speeds -= pq.top();
                    pq.pop();
                }

                sum_speeds += speed[cur_idx];
                pq.push(speed[cur_idx]);
                max_performance = max(max_performance, sum_speeds * (long long)efficiency[cur_idx]);
            }
        }

        return (int)(max_performance % MOD);
    }
};