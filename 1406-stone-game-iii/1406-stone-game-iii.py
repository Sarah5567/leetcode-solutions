class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * n

        for i in range(n - 1, -1, -1):
            picked_sum = 0
            for k in range(i, min(i + 3, n)):
                picked_sum += stoneValue[k]
                opponent_advantage = dp[k + 1] if k + 1 < n else 0
                dp[i] = max(dp[i], picked_sum - opponent_advantage)

        return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"
