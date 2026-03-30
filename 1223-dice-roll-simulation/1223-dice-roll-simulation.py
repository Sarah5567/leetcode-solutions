class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        LARGEST_NUM = 6
        
        dp = [[[0] * (rollMax[num] + 1) for num in range(LARGEST_NUM)] for _ in range(n)]
        total = [[0] * LARGEST_NUM for _ in range(n)]
        
        for num in range(LARGEST_NUM):
            dp[0][num][0] = 1
            total[0][num] = 1
        
        for length in range(1, n):
            for num in range(LARGEST_NUM):
                dp[length][num][0] = (sum(total[length - 1]) - total[length - 1][num]) % MOD
                
                for consecutive_n in range(1, rollMax[num]):
                    dp[length][num][consecutive_n] = dp[length - 1][num][consecutive_n - 1] % MOD
                
                total[length][num] = sum(dp[length][num]) % MOD
        
        return sum(total[-1]) % MOD