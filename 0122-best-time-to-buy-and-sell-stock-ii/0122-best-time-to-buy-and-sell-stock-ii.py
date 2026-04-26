class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cost = prices[0]
        last_transaction = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                last_transaction = prices[i] - cost
            else:
                profit += last_transaction
                last_transaction = 0
                cost = prices[i]

        return profit + last_transaction
