class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * min(i, query_glass + 1) for i in range(1, query_row + 2)]
        dp[0][0] = float(poured)

        for i in range(1, query_row + 1):
            all_zeros = True
            for j in range(len(dp[i])):
                val = 0.0

                if j < len(dp[i - 1]):
                    val += max(0.0, dp[i - 1][j] - 1.0) / 2.0
                if j > 0:
                    val += max(0.0, dp[i - 1][j - 1] - 1.0) / 2.0

                dp[i][j] = val
                all_zeros = all_zeros and val == 0.0
            if all_zeros:
                return 0.0

        return min(1.0, dp[query_row][query_glass])
        
