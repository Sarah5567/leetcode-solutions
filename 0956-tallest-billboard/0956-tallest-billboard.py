class Solution:
    def tallestBillboard(self, rods):
        S = sum(rods)
        OFFSET = S
        dp = [-1] * (2 * S + 1)
        dp[OFFSET] = 0

        for rod in rods:
            new_dp = dp[:]
            for d in range(-S, S + 1):
                if dp[d + OFFSET] == -1:
                    continue

                h = dp[d + OFFSET]

                nd = d + rod
                if -S <= nd <= S:
                    new_dp[nd + OFFSET] = max(new_dp[nd + OFFSET], h)

                nd = d - rod
                if -S <= nd <= S:
                    new_dp[nd + OFFSET] = max(new_dp[nd + OFFSET], h + rod)

            dp = new_dp

        return max(0, dp[OFFSET])
