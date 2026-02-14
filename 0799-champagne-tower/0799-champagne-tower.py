class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * (query_glass + 2)
        dp[0] = float(poured)

        for i in range(query_row):
            next_dp = [0.0] * (query_glass + 2)
            all_zeros = True

            upper = min(i + 1, query_glass)
            for j in range(upper + 1):
                overflow = max(0.0, dp[j] - 1.0) / 2.0
                if overflow:
                    next_dp[j] += overflow
                    next_dp[j + 1] += overflow
                    all_zeros = False

            if all_zeros:
                return 0.0
            dp = next_dp

        return min(1.0, dp[query_glass])