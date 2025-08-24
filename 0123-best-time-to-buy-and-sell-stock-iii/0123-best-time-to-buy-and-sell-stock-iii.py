class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n

        for _ in range(2): 
            diff = float('-inf')
            prev = 0
            for i, price in enumerate(prices):
                diff = max(diff, prev - price)
                prev = dp[i]
                if i > 0:
                    dp[i] = max(dp[i-1], diff + price)
                else:
                    dp[i] = max(dp[i], diff + price)

        return dp[-1]