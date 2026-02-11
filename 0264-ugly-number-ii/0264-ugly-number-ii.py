class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        
        pointers = [0, 0, 0]
        fectors = [2, 3, 5]

        for currIdx in range(1, n):
            dp[currIdx] = min(dp[i] * f for i, f in zip(pointers, fectors))
            for i in range(3):
                if dp[pointers[i]] * fectors[i] == dp[currIdx]:
                    pointers[i] += 1

        return dp[n - 1]
