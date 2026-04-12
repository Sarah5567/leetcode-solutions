class Solution:

    # DSU used to group connected 1-cells and compute island sizes
    class DisjointSet:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, a, b):
            rootA = self.find(a)
            rootB = self.find(b)

            if rootA == rootB:
                return

            if self.size[rootA] < self.size[rootB]:
                rootA, rootB = rootB, rootA

            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]

        def group_size(self, x):
            return self.size[self.find(x)]

        def same_group(self, a, b):
            return self.find(a) == self.find(b)
            

    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dsu = Solution.DisjointSet(m * n)

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def idx(r, c):
            return r * n + c

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dr, dc in moves:
                        ni, nj = i + dr, j + dc
                        if valid(ni, nj) and grid[ni][nj] == 1:
                            dsu.union(idx(i, j), idx(ni, nj))

        best = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    best = max(best, dsu.group_size(idx(i, j)))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    cur = 1

                    for dr, dc in moves:
                        ni, nj = i + dr, j + dc
                        if valid(ni, nj) and grid[ni][nj] == 1:
                            root = dsu.find(idx(ni, nj))
                            if root not in seen:
                                seen.add(root)
                                cur += dsu.size[root]

                    best = max(best, cur)

        return best
