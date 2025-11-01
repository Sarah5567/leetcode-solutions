class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dpLen = len(costs) + 1
        dp : List[int] = [float('inf') for _ in range(dpLen)]
        dp[0] = 0

        for i in range(0, dpLen - 1):
            for j in range(i + 1, i + 4):
                if j < dpLen:
                    dp[j] = min(dp[j], dp[i] + costs[j - 1] + (j - i) ** 2)

        return dp[dpLen - 1]