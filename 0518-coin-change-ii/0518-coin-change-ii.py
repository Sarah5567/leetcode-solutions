class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amounts = [0] * (amount + 1)
        amounts[0] = 1

        for coin in coins:
            for cur_amount in range(amount):
                if cur_amount + coin <= amount:
                    amounts[cur_amount + coin] += amounts[cur_amount]
                else:
                    break

        return amounts[-1]
