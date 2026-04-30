class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [float('inf')] * (amount + 1)
        amounts[0] = 0

        for cur_amount in range(amount):
            for coin in coins:
                if cur_amount + coin <= amount:
                    amounts[cur_amount + coin] = min(amounts[cur_amount + coin], amounts[cur_amount] + 1)

        return amounts[amount] if amounts[amount] < float('inf') else -1
