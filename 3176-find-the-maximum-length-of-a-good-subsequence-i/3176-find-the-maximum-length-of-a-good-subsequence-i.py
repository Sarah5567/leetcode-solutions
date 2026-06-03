class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prev_index = {}
        dp = [0] * n
        max_length = 0

        for _ in range(k + 1):
            next_dp = [0] * n
            prev_max = 0
            for i, num in enumerate(nums):
                next_dp[i] = max(dp[i], prev_max + 1)
                if num in prev_index:
                    next_dp[i] = max(next_dp[i], next_dp[prev_index[num]] + 1)

                prev_index[num] = i
                max_length = max(max_length, next_dp[i])
                prev_max = max(prev_max, dp[i])

            dp = next_dp
            prev_index = {}

        return max_length
