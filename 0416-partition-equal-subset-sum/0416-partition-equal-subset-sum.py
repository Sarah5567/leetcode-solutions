class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2:
            return False

        n, m = nums_sum // 2 + 1, len(nums) + 1
        dp = [[False] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = True

        for i in range(1, m):
            val = nums[i - 1]
            for j in range(1, n):
                dp[i][j] = (val <= j and dp[i - 1][j - val]) or dp[i - 1][j]

        return dp[-1][-1]