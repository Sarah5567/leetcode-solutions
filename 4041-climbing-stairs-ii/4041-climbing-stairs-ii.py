class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dpLen = len(costs) + 1
        dp : List[int] = [float('inf') for _ in range(dpLen)]
        dp[0] = 0

        for j in range(0, dpLen):
            for i in range(j - 3, j):
                if i >= 0:
                    dp[j] = min(dp[j], dp[i] + costs[j - 1] + (j - i) ** 2)

        return dp[dpLen - 1]