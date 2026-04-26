class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        sold = 0
        prev_sold = 0
        
        for price in prices:
            new_hold = max(hold, prev_sold - price)
            new_sold = max(sold, hold + price)

            hold, sold, prev_sold = new_hold, new_sold, sold

        return max(sold, prev_sold)
