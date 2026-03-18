class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 1 if grid[0][0] <= k else 0

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            if grid[i][0] <= k:
                count += 1

        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
            if grid[0][i]<= k:
                count += 1

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]
                if grid[i][j] <= k:
                    count += 1

        return count
