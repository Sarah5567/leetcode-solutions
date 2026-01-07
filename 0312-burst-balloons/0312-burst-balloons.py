class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        for i in range(2, n):
            for r, c in zip(range(n), range(i, n)):
                for j in range(r + 1, c):
                    dp[r][c] = max(dp[r][c], dp[r][j] + dp[j][c] + nums[r] * nums[j] * nums[c])

        return dp[0][n - 1]