class Solution {
public:
    class DisjointSet {
    private:
        vector<int> parent, rank;

    public:
        DisjointSet(int n) : parent(n), rank(n, 0) {
            for (int i = 0; i < n; i++)
                parent[i] = i;
        }

        int find(int x) {
            if (parent[x] != x)
                parent[x] = find(parent[x]);
            return parent[x];
        }

        void unite(int x, int y) {
            int rx = find(x);
            int ry = find(y);
            if (rx == ry) return;

            if (rank[rx] < rank[ry])
                parent[rx] = ry;
            else if (rank[rx] > rank[ry])
                parent[ry] = rx;
            else {
                parent[ry] = rx;
                rank[rx]++;
            }
        }
    };

    vector<bool> areConnected(int n, int threshold, vector<vector<int>>& queries) {
        DisjointSet ds(n + 1);
        for(int i = threshold + 1; i <= n; i++){
            for (int j = i * 2; j <= n; j += i)
                ds.unite(i, j);
        }
        vector<bool> res(queries.size());
        for(int i = 0; i < queries.size(); i++)
            res[i] = ds.find(queries[i][0]) == ds.find(queries[i][1]);
        return res;
    }
};