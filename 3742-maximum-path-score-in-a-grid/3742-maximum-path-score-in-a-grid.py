class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = 0

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    if (i > 0 and not dp[i - 1][j]) or (j > 0 and not dp[i][j - 1]):
                        dp[i][j] = 0

        max_score = dp[-1][-1]

        for _ in range(k):
            prev = dp
            dp = [[-1] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i > 0:
                        dp[i][j] = max(dp[i][j], prev[i - 1][j], dp[i - 1][j] if not grid[i][j] else -1)
                    if j > 0:
                        dp[i][j] = max(dp[i][j], prev[i][j - 1], dp[i][j - 1] if not grid[i][j] else -1)

                    if dp[i][j] != -1:
                        dp[i][j] += grid[i][j]

            max_score = max(max_score, dp[-1][-1])

        return max_score
