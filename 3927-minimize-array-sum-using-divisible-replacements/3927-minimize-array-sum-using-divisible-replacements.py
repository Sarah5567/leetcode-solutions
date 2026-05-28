class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        max_val = max(nums)
        dp = [max_val + 1] * (max_val + 1)

        nums.sort()
        total_sum = 0

        for num in nums:
            total_sum += min(dp[num], num)
            if dp[num] <= num:
                continue

            dp[num] = num

            for i in range(num * 2, max_val + 1, num):
                dp[i] = min(dp[i], dp[num])

        return total_sum
