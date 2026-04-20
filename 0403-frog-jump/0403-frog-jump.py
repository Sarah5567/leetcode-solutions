class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        dp = [set() for _ in range(n)]
        dp[0].add(0)

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                k = stones[i] - stones[j]
                if k > j + 1:
                    break

                if k in dp[j] or k - 1 in dp[j] or k + 1 in dp[j]:
                    dp[i].add(k)

        return bool(dp[-1])
