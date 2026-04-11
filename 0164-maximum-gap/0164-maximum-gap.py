class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0

        bucket_size = ceil((max_val - min_val) / (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        min_bucket = [inf] * bucket_count
        max_bucket = [-inf] * bucket_count
        used = [False] * bucket_count

        for num in nums:
            idx = (num - min_val) // bucket_size
            min_bucket[idx] = min(min_bucket[idx], num)
            max_bucket[idx] = max(max_bucket[idx], num)
            used[idx] = True

        gap = 0
        prev_max = min_val

        for i in range(bucket_count):
            if not used[i]:
                continue
            gap = max(gap, min_bucket[i] - prev_max)
            prev_max = max_bucket[i]

        return gap
