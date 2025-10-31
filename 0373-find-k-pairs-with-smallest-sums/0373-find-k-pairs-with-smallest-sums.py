class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = {(0, 0)}
        result : List[List[int]] = []
        heap = []
        heapq.heappush(heap, (nums1[0] + nums2[0], (0, 0)))
        for _ in range(k):
            _, (n1, n2) = heapq.heappop(heap)
            result.append([nums1[n1], nums2[n2]])
            if n1 < len(nums1) - 1 and (n1 + 1, n2) not in pairs:
                pairs.add((n1 + 1, n2))
                heapq.heappush(heap, (nums1[n1 + 1] + nums2[n2], (n1 + 1, n2)))
            if n2 < len(nums2) - 1 and (n1, n2 + 1) not in pairs:
                pairs.add((n1, n2 + 1))
                heapq.heappush(heap, (nums1[n1] + nums2[n2 + 1], (n1, n2 + 1)))

        return result
