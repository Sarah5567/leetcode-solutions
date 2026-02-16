class Solution:
    def strangePrinter(self, s: str) -> int:
        compressed: list[str] = []
        for ch in s:
            if not compressed or ch != compressed[-1]:
                compressed.append(ch)

        n = len(compressed)

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                dp[i][j] = dp[i][j - 1] + 1

                for k in range(i, j):
                    if compressed[k] == compressed[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + (dp[k + 1][j - 1] if k + 1 <= j - 1 else 0))

        return dp[0][n - 1]