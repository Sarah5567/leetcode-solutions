class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = nums[-1] - nums[0]

        for i in range(len(nums) - 1):
            diff = max(nums[i] + k, nums[-1] - k) - min(nums[i + 1] - k, nums[0] + k)
            min_diff = min(min_diff, diff)

        return min_diff
