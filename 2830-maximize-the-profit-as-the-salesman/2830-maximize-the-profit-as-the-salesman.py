class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda o:o[1])

        dp = [0] * n
        offer_idx = 0

        for house in range(n):
            dp[house] = dp[house - 1] if house else 0

            while offer_idx < len(offers) and offers[offer_idx][1] == house:
                start, end, gold = offers[offer_idx]
                dp[house] = max(dp[house], (dp[start - 1] if start else 0) + gold)
                offer_idx += 1

        return dp[-1]
