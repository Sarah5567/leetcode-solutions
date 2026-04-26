class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        with_shared = float('-inf')
        without_shared = 0

        for price in prices:
            with_shared, without_shared = max(with_shared, without_shared - price - fee), max(without_shared, with_shared + price)

        return without_shared
