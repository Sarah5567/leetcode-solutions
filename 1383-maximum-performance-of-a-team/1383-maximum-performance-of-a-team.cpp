class Solution {
private:
    void sort_by_second_desc(std::vector<int>& a, std::vector<int>& b) {
        int n = a.size();
        std::vector<int> idx(n);
        std::iota(idx.begin(), idx.end(), 0);

        std::sort(idx.begin(), idx.end(),
                [&](int i, int j) {
                    return b[i] > b[j];
                });

        auto apply = [&](std::vector<int>& v) {
            std::vector<int> tmp(n);
            for (int i = 0; i < n; i++)
                tmp[i] = v[idx[i]];
            v.swap(tmp);
        };

        apply(a);
        apply(b);
    }
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        const int MOD = 1'000'000'007;

        sort_by_second_desc(speed, efficiency);

        priority_queue<int, vector<int>, greater<int>> pq;
        pq.push(speed[0]);

        long long max_performance = speed[0] * (long long)efficiency[0];
        long long sum_speeds = speed[0];

        for(int i = 1; i < n; i++){
            if(i < k || pq.top() <= speed[i]){
                if(i >= k){
                    sum_speeds -= pq.top();
                    pq.pop();
                }

                sum_speeds += speed[i];
                pq.push(speed[i]);
                max_performance = max(max_performance, sum_speeds * (long long)efficiency[i]);
            }
        }

        return (int)(max_performance % MOD);
    }
};