class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2:
            return False

        n = nums_sum // 2 + 1
        dp = [False] * n
        dp[0] = True

        for num in nums:
            for i in range(n - 1, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                
        return dp[-1]