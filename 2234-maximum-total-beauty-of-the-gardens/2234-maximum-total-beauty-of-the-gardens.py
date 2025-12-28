class Solution:
    def maximumBeauty(
        self,
        flowers: List[int],
        newFlowers: int,
        target: int,
        full: int,
        partial: int
    ) -> int:

        n = len(flowers)

        flowers = [min(f, target) for f in flowers]
        flowers.sort()

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + flowers[i]

        def cost_to_reach(i: int, x: int) -> int:
            return x * (i + 1) - prefix[i + 1]

        res = 0

        if flowers[0] >= target:
            return n * full

        for complete in range(n + 1):
            if complete > 0:
                need = target - flowers[n - complete]
                newFlowers -= need
                if newFlowers < 0:
                    break

            if complete == n:
                res = max(res, n * full)
                continue

            left, right = flowers[0], target - 1
            best = flowers[0]

            while left <= right:
                mid = (left + right) // 2
                idx = bisect.bisect_right(flowers, mid, 0, n - complete) - 1

                if idx < 0:
                    cost = 0
                else:
                    cost = cost_to_reach(idx, mid)

                if cost <= newFlowers:
                    best = mid
                    left = mid + 1
                else:
                    right = mid - 1

            beauty = complete * full + best * partial
            res = max(res, beauty)

        return res
