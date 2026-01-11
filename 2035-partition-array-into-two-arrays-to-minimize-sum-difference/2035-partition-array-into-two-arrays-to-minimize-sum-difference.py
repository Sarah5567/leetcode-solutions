class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        half = n // 2
        total_sum = sum(nums)
        target = total_sum // 2

        left = nums[:half]
        right = nums[half:]

        sums_left = [[] for _ in range(half + 1)]
        sums_right = [[] for _ in range(half + 1)]

        for k in range(half + 1):
            for comb in combinations(left, k):
                sums_left[k].append(sum(comb))
            for comb in combinations(right, k):
                sums_right[k].append(sum(comb))

            sums_right[k].sort()

        ans = float('inf')

        for k in range(half + 1):
            left_sums = sums_left[k]
            right_sums = sums_right[half - k]

            for s1 in left_sums:
                need = target - s1
                idx = bisect_left(right_sums, need)

                for j in (idx, idx - 1):
                    if 0 <= j < len(right_sums):
                        diff = abs(total_sum - 2 * (s1 + right_sums[j]))
                        if diff < ans:
                            ans = diff
                            if ans == 0:
                                return 0

        return ans
