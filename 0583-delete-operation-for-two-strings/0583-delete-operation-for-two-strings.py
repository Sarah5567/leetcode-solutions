class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev_dp = [i for i in range(n + 1)]

        for i in range(m):
            dp = [0] * (n + 1)
            dp[0] = i + 1
            for j in range(n):
                dp[j + 1] = min(dp[j] + 1, prev_dp[j + 1] + 1, prev_dp[j] + 2)
                if word1[i] == word2[j]:
                    dp[j + 1] = min(dp[j + 1], prev_dp[j])
            
            prev_dp = dp

        return dp[-1]
