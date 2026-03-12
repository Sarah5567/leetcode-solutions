class DisjointSet {
private:
    std::vector<int> parent;
    std::vector<int> rank;
    int setCount;

public:
    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        setCount = n;

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unite(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA == rootB) {
            return;
        }

        if (rank[rootA] < rank[rootB]) {
            parent[rootA] = rootB;
        }
        else if (rank[rootA] > rank[rootB]) {
            parent[rootB] = rootA;
        }
        else {
            parent[rootB] = rootA;
            rank[rootA]++;
        }

        setCount--;
    }

    bool connected(int a, int b) {
        return find(a) == find(b);
    }

    int count() const {
        return setCount;
    }
};

class Solution {
private:
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int countZeros = 0;
        DisjointSet ds(m * n);

        auto getCellNum = [&](int r, int c) {
            return r * n + c;
        };

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '1'){
                    if(i > 0 && grid[i - 1][j] == '1')
                        ds.unite(getCellNum(i, j), getCellNum(i - 1, j));
                    if(j > 0 && grid[i][j - 1] == '1')
                        ds.unite(getCellNum(i, j), getCellNum(i, j - 1));
                }
                else{
                    countZeros++;
                }
            }
        }

        return ds.count() - countZeros;
    }
};