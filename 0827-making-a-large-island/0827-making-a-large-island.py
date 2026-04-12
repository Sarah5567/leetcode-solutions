class Solution:

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
                return rootA

            if self.size[rootA] < self.size[rootB]:
                rootA, rootB = rootB, rootA

            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]

            return rootA

    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dsu = Solution.DisjointSet(m * n)

        moves = [(0, 1), (1, 0)]

        def idx(r, c):
            return r * n + c

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        best = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    best = max(best, 1)
                    for dr, dc in moves:
                        ni, nj = i + dr, j + dc
                        if valid(ni, nj) and grid[ni][nj] == 1:
                            root = dsu.union(idx(i, j), idx(ni, nj))
                            best = max(best, dsu.size[root])

        root_grid = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    root_grid[i][j] = dsu.find(idx(i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = []
                    cur = 1

                    for dr, dc in directions:
                        ni, nj = i + dr, j + dc
                        if valid(ni, nj) and grid[ni][nj] == 1:
                            root = root_grid[ni][nj]
                            if root not in seen:
                                seen.append(root)
                                cur += dsu.size[root]

                    best = max(best, cur)

        return best
