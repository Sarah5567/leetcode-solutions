class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 1000000007
        dp = [[1 if i in [0, m + 1] or j in [0, n + 1] else 0
                for j in range(n + 2)]
                for i in range(m + 2)]
        paths = 0

        for _ in range(maxMove):
            next_dp = [[0] * (n + 2) for _ in range(m + 2)]

            for i in range(m):
                for j in range(n):
                    next_dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 2][j + 1] + dp[i + 1][j] + dp[i + 1][j + 2]

            dp = next_dp
            paths += dp[startRow + 1][startColumn + 1]

        return  paths % MOD
