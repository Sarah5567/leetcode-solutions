class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        last_transaction = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                last_transaction = prices[i] - buy
            else:
                profit += last_transaction
                last_transaction = 0
                buy = prices[i]

        return profit + last_transaction
