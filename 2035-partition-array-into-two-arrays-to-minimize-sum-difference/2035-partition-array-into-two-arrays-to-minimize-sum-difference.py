class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        half = n // 2
        total_sum = sum(nums)

        left = nums[:half]
        right = nums[half:]

        sums_left = [[] for _ in range(half + 1)]
        sums_right = [[] for _ in range(half + 1)]

        for mask in range(1 << half):
            cnt = 0
            s = 0
            for i in range(half):
                if mask & (1 << i):
                    cnt += 1
                    s += left[i]
            sums_left[cnt].append(s)

        for mask in range(1 << half):
            cnt = 0
            s = 0
            for i in range(half):
                if mask & (1 << i):
                    cnt += 1
                    s += right[i]
            sums_right[cnt].append(s)

        for k in range(half + 1):
            sums_right[k].sort()

        ans = float('inf')
        target = total_sum // 2

        for k in range(half + 1):
            left_sums = sums_left[k]
            right_sums = sums_right[half - k]

            for s1 in left_sums:
                need = target - s1
                idx = bisect_left(right_sums, need)

                for j in (idx, idx - 1):
                    if 0 <= j < len(right_sums):
                        s2 = right_sums[j]
                        chosen = s1 + s2
                        other = total_sum - chosen
                        ans = min(ans, abs(chosen - other))

        return ans
