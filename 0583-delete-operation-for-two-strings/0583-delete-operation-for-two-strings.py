class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            dp[0][i] = i

        for i in range(m):
            dp[i + 1][0] = i + 1
            for j in range(n):
                dp[i + 1][j + 1] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i][j] + 2)
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])

        return dp[-1][-1]
