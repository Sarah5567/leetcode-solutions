class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)

        diffs = Counter(abs(nums1[i] - nums2[i]) for i in range(n))

        max_heap = [[-diff, freq] for diff, freq in diffs.items() if diff > 0]
        heapq.heapify(max_heap)

        remaining = k1 + k2

        while remaining > 0 and max_heap:
            diff, freq = heapq.heappop(max_heap)
            diff = -diff

            next_diff = -max_heap[0][0] if max_heap else 0

            needed = (diff - next_diff) * freq

            if needed <= remaining:
                remaining -= needed

                if next_diff > 0:
                    max_heap[0][1] += freq
            else:
                full = remaining // freq
                extra = remaining % freq

                new_diff = diff - full

                if new_diff > 0:
                    heapq.heappush(max_heap, [-new_diff, freq - extra])

                if new_diff - 1 > 0 and extra > 0:
                    heapq.heappush(max_heap, [-(new_diff - 1), extra])

                remaining = 0

        return sum(((-diff) ** 2) * freq for diff, freq in max_heap)