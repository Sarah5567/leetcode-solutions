class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]
        dp[0][0][0] = dp[0][1][0] = dp[0][0][1] = 1

        for i in range(1, n):
            dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0]) % MOD
            dp[i][1][0] = dp[i-1][0][0]
            dp[i][2][0] = dp[i-1][1][0]

            dp[i][0][1] = (dp[i-1][0][1] + dp[i-1][1][1] + dp[i-1][2][1] + dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0]) % MOD
            dp[i][1][1] = dp[i-1][0][1]
            dp[i][2][1] = dp[i-1][1][1]

        result = sum(dp[-1][l][a] for l in range(3) for a in range(2)) % MOD
        return result