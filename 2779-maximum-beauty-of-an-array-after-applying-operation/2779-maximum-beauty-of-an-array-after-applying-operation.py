class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_beauty, begin_idx = 0, 0
        for idx, num in enumerate(nums):
            begin_idx = bisect_left(nums, num - k * 2, lo=begin_idx, hi=idx)
            max_beauty = max(max_beauty, idx - begin_idx + 1)

        return max_beauty
