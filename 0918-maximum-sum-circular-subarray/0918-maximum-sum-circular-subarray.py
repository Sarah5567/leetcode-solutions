class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        min_sum = nums[0]
        total = 0

        for num in nums:
            total = min(total, 0) + num
            min_sum = min(min_sum, total)

        total_sum = sum(nums)
        if min_sum == total_sum:
            max_sum = nums[0]
        else:
            max_sum = total_sum - min_sum

        total = 0
        for num in nums:
            total = max(total, 0) + num
            max_sum = max(max_sum, total)

        return max_sum

