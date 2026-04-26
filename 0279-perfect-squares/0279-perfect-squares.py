class Solution:
    def numSquares(self, n: int) -> int:
        sums = [float('inf')] * (n + 1)
        sums[0] = 0
        n_square = int(n ** 0.5)

        for cur_sum in range(1, n + 1):
            for root in range(1, n_square + 1):
                square_number = root * root
                if square_number <= cur_sum:
                    sums[cur_sum] = min(sums[cur_sum], sums[cur_sum - square_number] + 1)

        return sums[n]
