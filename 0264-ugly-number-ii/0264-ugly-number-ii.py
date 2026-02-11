class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        p2 = p3 = p5 = 0
        next2, next3, next5 = 2, 3, 5

        for i in range(1, n):
            x = min(next2, next3, next5)
            dp[i] = x

            if x == next2:
                p2 += 1
                next2 = dp[p2] * 2
            if x == next3:
                p3 += 1
                next3 = dp[p3] * 3
            if x == next5:
                p5 += 1
                next5 = dp[p5] * 5

        return dp[-1]
