class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [float('inf')] * (amount + 1)
        amounts[0] = 0

        coins.sort()

        for cur_amount in range(1, amount + 1):
            for coin in coins:
                if cur_amount - coin >= 0:
                    amounts[cur_amount] = min(amounts[cur_amount - coin] + 1, amounts[cur_amount])
                else:
                    break

        return amounts[amount] if amounts[amount] < float('inf') else -1
