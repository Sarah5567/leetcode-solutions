class Solution:
    def splitArray(self, nums, k):
        n = len(nums)

        # prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # dp[i][j] = minimum largest-sum when splitting first j elements into i parts
        INF = 10**18
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0   # 0 parts, 0 elements = valid

        for i in range(1, k + 1):
            for j in range(i, n + 1):          # at least i elements needed
                # try all split points t < j
                for t in range(i - 1, j):
                    left = dp[i - 1][t]
                    right = prefix[j] - prefix[t]
                    dp[i][j] = min(dp[i][j], max(left, right))

        return dp[k][n]
