class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        n, r = max(n, r), min(n, r)

        dp = [True] * (n + 1)
        dp[0] = dp[1] = False

        num = 2
        while num * num <= n:
            if dp[num]:
                for i in range(num * num, n + 1, num):
                    dp[i] = False

            num += 1

        return sum(i for i in range(r, n + 1) if dp[i])
