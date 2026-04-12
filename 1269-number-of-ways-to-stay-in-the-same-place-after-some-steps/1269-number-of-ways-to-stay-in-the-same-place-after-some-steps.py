class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 1000000007

        dp_len = min(arrLen, steps // 2 + 1)
        dp = [0] * dp_len
        dp[0] = 1

        for step in range(steps):
            prev_dp = dp
            dp = prev_dp[:]

            if dp_len > 1:
                dp[0] = (dp[0] + prev_dp[1]) % MOD
                dp[-1] = (dp[-1] + prev_dp[-2]) % MOD

            for i in range(1, dp_len - 1):
                dp[i] = (dp[i] + prev_dp[i - 1] + prev_dp[i + 1]) % MOD

        return dp[0] 
            

            

        